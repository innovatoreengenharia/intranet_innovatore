var imagem_original;
var nome_imagem_original;
// Carregar o espaço para o preview da imagem.
var redimensionar_destaque = $('#preview_destaque').croppie({
    // Ativar a leitura de orientação para renderizar corretamente a imagem.
    enableExif: true,

    // Ativar a orientação personalizada.
    enableOrientation: true,

    // O recipiente interno do coppie. A parte visíval da imagem.
    viewport:{
        width: 510,
        height: 166,
        type: 'square'
    },

    // O recipiente externo do coppie. A parte visíval da imagem.
    boundary: { 
        width: 610, 
        height: 266
    },
});


// 16 X 9


var redimensionar_thumb = $('#preview_thumb').croppie({
    // Ativar a leitura de orientação para renderizar corretamente a imagem.
    enableExif: true,

    // Ativar a orientação personalizada.
    enableOrientation: true,

    // O recipiente interno do coppie. A parte visíval da imagem.
    viewport:{
        width: 364,
        height: 240,
        type: 'square'
    },

    // O recipiente externo do coppie. A parte visíval da imagem.
    boundary: { 
        width: 464, 
        height: 340
    },
});

// 21 X 9

var redimensionar_noticia = $('#preview_noticia').croppie({
    // Ativar a leitura de orientação para renderizar corretamente a imagem.
    enableExif: true,

    // Ativar a orientação personalizada.
    enableOrientation: true,

    // O recipiente interno do coppie. A parte visíval da imagem.
    viewport:{
        width: 433,
        height: 157,
        type: 'square'
    },

    // O recipiente externo do coppie. A parte visíval da imagem.
    boundary: { 
        width: 533, 
        height: 257
    },
});


// Executar a instrução quando o usuário selcionar uma imagem.
$('#imagem').on('change', function(){

    // FileReader para ler de forma assíncrona o conteúdo do arquivo.
    var reader = new FileReader();

    // onload - execute após ler o conteúdo.
    reader.onload = function(e){

        imagem_original = e.target.result;

        redimensionar_destaque.croppie('bind', {
            url: e.target.result
        });
        redimensionar_thumb.croppie('bind', {
            url: e.target.result
        });
        redimensionar_noticia.croppie('bind', {
            url: e.target.result
        })
    }
    nome_imagem_original = this.files[0].name    
     // O método  readAsDataURL é usado para ler conteúdo do tipo Blob ou File.
     reader.readAsDataURL(this.files[0]);

});
var blocos = [];
    
// criar uma variavel imagens contendo um objeto com chave e valor, sendo chave o objeto que ela pertence e valor a imagem
var imagens = {};
var nomes_de_imagens = {}
// fazer uma query nos imagem_bloco
$(".imagem_bloco").on('change', function() {
    var name = this.name
    var index = name.replace("bloco_set-", "").replace("-imagem_bloco", "")
    // criar um evento de on change
    var reader = new FileReader();
    reader.onload = function(e){
        imagem = e.target.result
        // adicionar a imagem ao dicionario de imagens
        imagens[index] = imagem
    }
    nomes_de_imagens[index] = this.files[0].name
    reader.readAsDataURL(this.files[0])
})
$(".btn-upload-imagem").on("click", async function(){

    //Verifica se a imagem é destaque:
    var destaque_js = $("#destaque").prop("checked");
    var destaque_checkbox = destaque_js ? "True" : "False";

    var titulo = $("#titulo").val();
    
    var paragrafo = $("#paragrafo").val();
    
    var tags = $("#tags").val();

    var imagem = imagem_original;

    var destaque = await redimensionar_destaque.croppie('result',{
        type: "canvas",
        size: "original"
    });

    var thumb = await redimensionar_thumb.croppie('result',{
        type: "canvas",
        size: "original"
    });

    var noticia = await redimensionar_noticia.croppie('result',{
        type: "canvas",
        size: "original"
    });
    $('.inline-bloco').each(function(index, element) {
        blocos.push({
            imagem_bloco: imagens[index],
            nome_imagem_bloco: nomes_de_imagens[index],
            titulo_bloco: $(element).find('[name$=titulo_bloco]').val(),
            paragrafo_bloco: $(element).find('[name$=paragrafo_bloco]').val(),
        });
    });
    
    $.ajax({
        url:"/informativos/add_noticia/",
        type: "POST",
        data: {
            "titulo": titulo,
            "paragrafo": paragrafo,
            "tags": tags,
            "nome_imagem": nome_imagem_original,
            "imagem": imagem,
            "nome_imagem_destaque": "destaque_" + nome_imagem_original,
            "imagem_destaque": destaque,
            "nome_imagem_thumb": "thumb_" + nome_imagem_original,
            "imagem_thumb": thumb,
            "nome_imagem_noticia": "noticia_" + nome_imagem_original,
            "imagem_noticia": noticia,
            "destaque_checkbox": destaque_checkbox,
            "blocos": JSON.stringify(blocos),
        },
        success:function(){


            $("#titulo").val("");
            $("#paragrafo").val("");
            $("#tags").val("");
            $("#imagem").val("");
            $("#preview_destaque").val("");
            $("#preview_thumb").val("");
            $("#preview_noticia").val("");
            $("#destaque").prop("checked", false);

            alert("Imagens enviadas com sucesso");
            
        }
    }); 
});