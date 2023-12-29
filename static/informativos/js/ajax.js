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

$(".btn-upload-imagem").on("click", async function(){

    var formData = new FormData();

    //Verifica se a imagem é destaque:

    formData.append("titulo", $("#titulo").val());
    formData.append("paragrafo", $("#paragrafo").val());
    formData.append("tags", $("#tags").val());
    formData.append("destaque_checkbox", $("#destaque").prop("checked"));

    var imagemInput = $("#imagem")[0];
    if (imagemInput.files.length > 0) {
        formData.append("imagem", imagemInput.files[0]);
    }

    var destaque = await redimensionar_destaque.croppie('result',{
        type: "canvas",
        size: "original"
    });
    formData.append("imagem_destaque", dataURLtoFile(destaque, "destaque.jpg"));

    var thumb = await redimensionar_thumb.croppie('result',{
        type: "canvas",
        size: "original"
    });
    formData.append("imagem_thumb", dataURLtoFile(thumb, "thumb.jpg"));

    var noticia = await redimensionar_noticia.croppie('result',{
        type: "canvas",
        size: "original"
    });
    formData.append("imagem_noticia", dataURLtoFile(noticia, "noticia.jpg"));

    formData.append("nome_imagem", nome_imagem_original);
    formData.append("nome_imagem_destaque", "destaque_" + nome_imagem_original);
    formData.append("nome_imagem_thumb", "thumb_" + nome_imagem_original);
    formData.append("nome_imagem_noticia", "noticia_" + nome_imagem_original);

    $('.inline-bloco').each(function(index, element) {
        formData.append(`formset_data[${index}][titulo_bloco]`, $(element).find('[name$=titulo_bloco]').val());
        formData.append(`formset_data[${index}][paragrafo_bloco]`, $(element).find('[name$=paragrafo_bloco]').val());

        var blocoInput = $(element).find('[name$=imagem_bloco]')[0];
        if (blocoInput.files.length > 0) {
            formData.append(`formset_data[${index}][imagem_bloco]`, blocoInput.files[0]);
        }
    });

    try {
        const response = await fetch("/informativos/add_noticia/", {
            method: "POST",
            body: formData
        });

        const responseData = await response.json();
        console.log(responseData);

        // Adicione aqui o que você quer fazer após o sucesso

    } catch (error) {
        console.error(error);
    }
});

function dataURLtoFile(dataURL, fileName) {
    var arr = dataURL.split(','),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]),
        n = bstr.length,
        u8arr = new Uint8Array(n);
        
    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }

    return new File([u8arr], fileName, { type: mime });
}