import json
from .models import Comentarios
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

        print(self.room_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

        print(f"disconecatdo; {self.room_name}")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_id = text_data_json['user']

        #TODO- alterar variavel aqui para nomear como perfil
        user = await get_user(user_id)

        post_id = text_data_json['post']
        texto_comentario = text_data_json['texto_comentario']

        #Send message to room group
        await self.channel_layer.group_send(
        self.room_group_name, {"type": "chat.texto_comentario", "texto_comentario": texto_comentario, "user": user}
        )
    
        

        # # Envie a mensagem de volta para todos os clientes conectados
        # await self.send(text_data=json.dumps({
        #     'status': 'Comentário salvo com sucesso!',
        #     'texto_comentario': texto_comentario
        # }))
        
        await self.salvar_comentario(user_id, post_id, texto_comentario)
        


    @database_sync_to_async
    def salvar_comentario(self, user_id, post_id, texto_comentario):
        # Salve o comentário no banco de dados usando seu modelo de dados
        comentario = Comentarios(user_id=user_id, post_id=post_id, texto_comentario=texto_comentario)
        comentario.save()

    

    async def chat_texto_comentario(self, event):
        texto_comentario = event["texto_comentario"]
        user = event["user"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"texto_comentario": texto_comentario, "user": user}))

    
@database_sync_to_async
def get_user(user_id):
    resultado_query = Perfil.objects.get(id=user_id)
    user = {
        'nome': resultado_query.nome,
        'sobrenome': resultado_query.sobrenome,
        'sexo': resultado_query.sexo,
    }
    if resultado_query.foto:
        user["foto_url"] = resultado_query.foto.url
        
    return user