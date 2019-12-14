window.onload=function(){
    secion02=document.getElementById("section02");
    secion02.style.display ='none';
}

document.getElementById("button1").onclick = function() {
    document.getElementById("section02").style.display = 'block';
}

document.getElementById("reload").onclick=function(){
   location.reload();
}