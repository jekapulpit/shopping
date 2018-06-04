
$(document).ready(function(){

    slider1  = $("#sliderphoto").lightSlider({
                loop:true,
                keyPress:true,
                item: 1,
                slideMargin: 0,
                pager: false,
                enableDrag: false,



            });



    });

function next1(){
slider1.goToNextSlide();
}
function prev1(){
    slider1.goToPrevSlide();

}