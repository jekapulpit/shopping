function showmenu() {
    if($(".menumobile").css("visibility") == "hidden"){
        $(".menumobile").css("visibility", "visible");
              $(".menu1").css("visibility", "hidden");
                $("body").css("overflow", "hidden");


    } else {
      $(".menumobile").css("visibility", "hidden");
    }
}

function showmenu1() {
    if($(".menu1").css("visibility") == "hidden"){
        $(".menu1").css("visibility", "visible");
        $(".menumobile").css("visibility", "hidden");
                $("body").css("overflow", "hidden");
        

    } else {
      $(".menu1").css("visibility", "hidden");
    }
}

function opis() {

  $("#opis1").addClass('active');
  $("#harak1").removeClass('active');

  el = document.getElementById("changetext");

  el.innerHTML = T;
}

function harak() {
  $("#harak1").addClass('active');
  $("#opis1").removeClass('active');
   el = document.getElementById("changetext");
el.innerHTML = '';

  if(size != ""){
    if(flag){
    size = '<p>Размеры: ' + size + '</p>';
  }
    el.innerHTML += size;
  } 
  if(matherial != "") {
     if(flag){
    matherial = '<p>Материал: ' + matherial + '</p>';
  }
 el.innerHTML += matherial;
  }
  if(color != "") {
     if(flag){
    color = '<p>Цвета: ' + color + '</p>';
  }
 el.innerHTML += color;

  } 
  if(qualities != "") {
     if(flag){
qualities = '<p>' + qualities + '</p>';
}
 el.innerHTML += qualities; 
  }
  flag = false;
}