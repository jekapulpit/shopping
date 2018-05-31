function showmenu(){
    if($(".menumobile").css("visibility") == "visible")
        $(".menumobile").css("visibility", "hidden");
    else {
            $(".menumobile").css("visibility", "visible");
    }
}