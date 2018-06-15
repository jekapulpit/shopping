
$(document).ready(function(){
    if($(window).width() < '767'){
        $("#hellopreloader_preload").css("background-size","30%");
    }
        if($(window).width() < '641'){
        $("#hellopreloader_preload").css("background-size","30%");
        slider1  = $("#content-slider2").lightSlider({
                loop:true,
                keyPress:true,
                item: 1,
                slideMargin: 15,
                pager: false,
                enableDrag: true,
                 
                 
            }); 
    

    }
    else {
    slider1  = $("#content-slider2").lightSlider({
                loop:true,
                keyPress:true,
                item: 3,
                slideMargin: 15,
                pager: false,
                enableDrag: true,
                 
                 
            }); 
    
        }
        
    });

function next1(){
slider1.goToPrevSlide();
}

function prev1(){
    slider1.goToNextSlide();

}