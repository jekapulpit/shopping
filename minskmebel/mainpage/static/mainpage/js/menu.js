function showmenu() {
    if($(".menumobile").css("visibility") == "hidden"){
        $(".menumobile").css("visibility", "visible");
              $(".menu1").css("visibility", "hidden");

    } else {
      $(".menumobile").css("visibility", "hidden");
    }
}

function showmenu1() {
    if($(".menu1").css("visibility") == "hidden"){
        $(".menu1").css("visibility", "visible");
        $(".menumobile").css("visibility", "hidden");

    } else {
      $(".menu1").css("visibility", "hidden");
    }
}

function opis() {
  $("#opis1").addClass('active');
  $("#harak1").removeClass('active');

  el = document.getElementById("changetext");

  el.innerHTML = M;
}

function harak() {
  $("#harak1").addClass('active');
  $("#opis1").removeClass('active');

   el = document.getElementById("changetext");
  el.innerHTML = T;
}