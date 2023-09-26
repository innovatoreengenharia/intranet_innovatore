$(function(){

    var numImages = 3;
    var MarginPadding = 135;
    var ident = 0;
    var count = numImages - 1;
    var slide = parseInt($('.carrossel .carrossel-item').outerWidth() + (MarginPadding * numImages));
    $('.next').click(function(){
        if (ident < count) {
            ident ++;
            $('.carrossel').animate({'margin-left': '-=' + slide + 'px'}, '500');
        }
        else{
            ident = 0;
            $('.carrossel').animate({'margin-left': '=' + 0 + 'px'}, '1000');
        }
    });
    $('.prev').click(function(){
        if (ident >= 1) {
            ident --;
            $('.carrossel').animate({'margin-left': '+=' + slide + 'px'}, '500');
        }
    });
    
});