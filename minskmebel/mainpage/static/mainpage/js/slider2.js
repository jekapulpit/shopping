
$(document).ready(function(){
    if($(window).width() < '767'){
        $("#hellopreloader_preload").css("background-size","30%");
    }
    slider  = $("#content-slider").lightSlider({
                loop:true,
                keyPress:true,
                item: 4,
                slideMargin: 15,
                pager: false,
                enableDrag: true,
                 
                 
            }); 
    
        
        
    });

function next(){
slider.goToPrevSlide();
}

function prev(){
    slider.goToNextSlide();

}