function getPhotoBySex(sexo) {
    if (sexo == 'feminino') {
        return `<img class="img-comentario" src="/static/usuario/img/avatar-f.jpeg">`
    } else {
        return `<img class="img-comentario" src="/static/usuario/img/avatar-m.jpeg">`
    }
}

function getUserPhoto(user) {
    if (user?.foto_url) {
        return `<img src="${user?.foto_url}" class="img-comentario">`
    } else {
        return getPhotoBySex(user?.sexo)
    }
}

function initializeChat(chatLogSelector, chatInputSelector, chatSubmitSelector, roomChatSelector, perfil_id, post_id) {
    const roomName = $(roomChatSelector).html();
    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/chat/'
        + roomName
        + '/'
    );

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        if (data?.texto_comentario) {
            // recebeu comentario
            const texto_comentario = data?.texto_comentario;
            const user = data?.user;
            const user_foto = getUserPhoto(user);
            const user_nome_completo = `${user?.nome} ${user?.sobrenome}`
            document.querySelector(chatLogSelector).innerHTML += `
                <div class="texto-comentario">
                    ${user_foto}
                    <p class="nome-comentario">${user_nome_completo}</p>
                    <p class="texto-comentario-p">${texto_comentario}</p>
                </div>
            `;
        } else {
            // recebeu like
            // verificar se é o próprio usuario que realizou a ação
            if (data?.user?.id == perfil_id) {
                // verifica se a acao foi de curtir ou descurtir para mudar o ícone e a classe
                if (data?.like?.acao == 'curtir') {
                    document.querySelector(`.like-vazio-${post_id} img`).src = "/static/social/img/like_preenchido.png"
                    document.querySelector(`.like-vazio-${post_id}`).classList.replace(`like-vazio-${post_id}`, `like-preenchido-${post_id}`)
                } else {
                    document.querySelector(`.like-preenchido-${post_id} img`).src = "/static/social/img/like.png"
                    document.querySelector(`.like-preenchido-${post_id}`).classList.replace(`like-preenchido-${post_id}`, `like-vazio-${post_id}`)
                }
            }
            // incrementa número de likes
            let likes_atual = parseInt(document.querySelector(`#likes-${post_id}`).innerHTML); 
            if (data?.like?.acao == 'curtir') {
                document.querySelector(`#likes-${post_id}`).innerHTML = likes_atual + 1
            }
            else {
                document.querySelector(`#likes-${post_id}`).innerHTML = likes_atual - 1
            }
        }
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector(chatInputSelector).onkeyup = function (e) {
        if (e.key === 'Enter') {  // Enter key
            document.querySelector(chatSubmitSelector).click();
        }
    };

    document.querySelector(chatSubmitSelector).onclick = function (e) {
        const messageInputDom = document.querySelector(chatInputSelector);
        const texto_comentario = messageInputDom.value;

        // Obtenha os detalhes do comentário
        const user = perfil_id;  // Obtenha o ID do usuário
        const post = post_id;    // Obtenha o ID do post

        // Crie um objeto com os detalhes do comentário e a mensagem
        const commentDetails = {
            'user': user,
            'post': post,
            'texto_comentario': texto_comentario
        };

        chatSocket.send(JSON.stringify(commentDetails)); // Envie os detalhes do comentário

        messageInputDom.value = ''
    };

    // FUNÇÃO DE LIKE

    $(document).on('click', `.like-vazio-${post_id}`, function () {
        const mensagem = {
            'user': perfil_id,
            'post': post_id,
            'like': {
                'acao': 'curtir'
            }
        }
        chatSocket.send(JSON.stringify(mensagem));
    });

    // FUNÇÃO DE DESLIKE

    $(document).on('click', `.like-preenchido-${post_id}`, function () {
        const mensagem = {
            'user': perfil_id,
            'post': post_id,
            'like': {
                'acao': 'descurtir'
            }
        }
        chatSocket.send(JSON.stringify(mensagem));
    });
}
