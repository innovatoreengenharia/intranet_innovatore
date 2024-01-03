// Obtém uma coleção de elementos com a classe "paragrafo_destaque_"
var paragrafos_destaque = document.getElementsByClassName("paragrafo-destaque");

// Itera sobre a coleção de parágrafos
for (var i = 0; i < paragrafos_destaque.length; i++) {
    var paragrafo = paragrafos_destaque[i];

    // Verifica se o elemento existe antes de acessar suas propriedades
    if (paragrafo) {
        var limite = 300; // Substitua pelo número desejado de caracteres

        // Verifica se o comprimento do conteúdo do parágrafo é maior que o limite
        if (paragrafo.innerHTML.length > limite) {
            paragrafo.innerHTML = paragrafo.innerHTML.substring(0, limite) + "...";
        }
    }
}

// Obtém uma coleção de elementos com a classe "paragrafo_thumb"
var paragrafos = document.getElementsByClassName("paragrafo_thumb");

// Itera sobre a coleção de parágrafos
for (var i = 0; i < paragrafos.length; i++) {
    var paragrafo = paragrafos[i];

    // Verifica se o elemento existe antes de acessar suas propriedades
    if (paragrafo) {
        var limite = 250; // Substitua pelo número desejado de caracteres

        // Verifica se o comprimento do conteúdo do parágrafo é maior que o limite
        if (paragrafo.innerHTML.length > limite) {
            paragrafo.innerHTML = paragrafo.innerHTML.substring(0, limite) + "...";
        }
    }
}

// Obtém uma coleção de elementos com a classe "paragrafo_destaque_"
var paragrafos_card = document.getElementsByClassName("paragrafo-card");

// Itera sobre a coleção de parágrafos
for (var i = 0; i < paragrafos_card.length; i++) {
    var paragrafo = paragrafos_card[i];

    // Verifica se o elemento existe antes de acessar suas propriedades
    if (paragrafo) {
        var limite = 100; // Substitua pelo número desejado de caracteres

        // Verifica se o comprimento do conteúdo do parágrafo é maior que o limite
        if (paragrafo.innerHTML.length > limite) {
            paragrafo.innerHTML = paragrafo.innerHTML.substring(0, limite) + "...";
        }
    }
}

var paragrafos_comunicado = document.getElementsByClassName("paragrafo-comunicado");

// Itera sobre a coleção de parágrafos
for (var i = 0; i < paragrafos_comunicado.length; i++) {
    var paragrafo = paragrafos_comunicado[i];

    // Verifica se o elemento existe antes de acessar suas propriedades
    if (paragrafo) {
        var limite = 200; // Substitua pelo número desejado de caracteres

        // Verifica se o comprimento do conteúdo do parágrafo é maior que o limite
        if (paragrafo.innerHTML.length > limite) {
            paragrafo.innerHTML = paragrafo.innerHTML.substring(0, limite) + "...";
        }
    }
}