$(document).ready(function () {
    $('a').click(function () {

        var ano = $(this).attr('class').split('-')[1]; // Pega o ano do parágrafo
        $('.ano-div').removeClass('mostrar'); // Remove a classe 'mostrar' de todas as divs
        $('#div-' + ano).addClass('mostrar'); // Adiciona a classe 'mostrar' à div correspondente ao ano clicado

        $('.ano-2015' ).css('font-weight', '400')
        $('.ano-2017' ).css('font-weight', '400')
        $('.ano-2019' ).css('font-weight', '400')
        $('.ano-2021' ).css('font-weight', '400')
        $('.ano-2022' ).css('font-weight', '400')
        $('.ano-2023' ).css('font-weight', '400')
        $(this).css('font-weight', '700')

        
    });
});