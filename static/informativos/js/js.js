function limitar_caracteres(classe, quantidade){
    var paragrafo_completo = document.getElementsByClassName(classe);

    // Itera sobre a coleção de parágrafos
    for (var i = 0; i < paragrafo_completo.length; i++) {
        var paragrafo = paragrafo_completo[i];

        // Verifica se o elemento existe antes de acessar suas propriedades
        if (paragrafo) {
            var limite = quantidade; // Substitua pelo número desejado de caracteres

            // Verifica se o comprimento do conteúdo do parágrafo é maior que o limite
            if (paragrafo.innerHTML.length > limite) {
                paragrafo.innerHTML = paragrafo.innerHTML.substring(0, limite) + "...";
            }
        }
    }
}

limitar_caracteres("paragrafo-destaque", 300);
limitar_caracteres("paragrafo_thumb", 250);
limitar_caracteres("paragrafo-card", 100);
limitar_caracteres("paragrafo-comunicado", 200);
limitar_caracteres("paragrafo-ultimo-quadro", 400);
limitar_caracteres("paragrafo-quadro", 250);