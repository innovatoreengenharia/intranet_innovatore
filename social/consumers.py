import json
from .models import Comentarios, Like
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from usuario.models import Perfil
from django.forms.models import model_to_dict


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

        print(f"desconecatdo; {self.room_name}")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_id = text_data_json["user"]

        perfil = await get_user(user_id)

        post_id = text_data_json["post"]

        if "texto_comentario" in text_data_json.keys():
            texto_comentario = text_data_json["texto_comentario"]
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.texto_comentario",
                    "texto_comentario": texto_comentario,
                    "user": perfil,
                },
            )
            await self.salvar_comentario(user_id, post_id, texto_comentario)
        else:
            like = text_data_json["like"]
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "chat.like", "like": like, "user": perfil},
            )
            await self.salvar_like(user_id, post_id, like)
        # Send message to room group

        # # Envie a mensagem de volta para todos os clientes conectados
        # await self.send(text_data=json.dumps({
        #     'status': 'Comentário salvo com sucesso!',
        #     'texto_comentario': texto_comentario
        # }))

    @database_sync_to_async
    def salvar_comentario(self, user_id, post_id, texto_comentario):
        # Salve o comentário no banco de dados usando seu modelo de dados
        comentario = Comentarios(
            user_id=user_id, post_id=post_id, texto_comentario=texto_comentario
        )
        comentario.save()

    @database_sync_to_async
    def salvar_like(self, user_id, post_id, like):
        if like.get("acao") == "curtir":
            like_bd = Like(user_id=user_id, post_id=post_id)
            like_bd.save()
        else:
            like_delete = Like.objects.get(user_id=user_id, post_id=post_id)
            like_delete.delete()

    async def chat_texto_comentario(self, event):
        texto_comentario = event["texto_comentario"]
        user = event["user"]
        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({"texto_comentario": texto_comentario, "user": user})
        )

    async def chat_like(self, event):
        like = event["like"]
        user = event["user"]
        await self.send(text_data=json.dumps({"like": like, "user": user}))


@database_sync_to_async
def get_user(user_id):
    resultado_query = Perfil.objects.get(id=user_id)
    user = {
        "nome": resultado_query.nome,
        "sobrenome": resultado_query.sobrenome,
        "sexo": resultado_query.sexo,
        "id": resultado_query.id,
    }
    if resultado_query.foto:
        user["foto_url"] = resultado_query.foto.url

    return user
