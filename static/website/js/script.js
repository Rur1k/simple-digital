$(document).ready(function() {
    $('.header__burger').click(function(event) {
     $('.header__burger,.header__menu').toggleClass('active');
     $('body').toggleClass('lock')
    }); 
 }); 


 $(document).ready(function(){
    $(window).scroll(function(){
        if($(window).scrollTop() > 500){
            $(".header").css({"background-color":"black"});   
        }
        else{
            $(".header").css({"background-color":""});
        }

    })
})