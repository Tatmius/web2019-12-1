window.onload=function(){
    secion02=document.getElementById("section02");
    secion02.style.display ='none';
}

document.getElementById("button1").onclick = function() {
    getElementById("section02").style.display = 'block';
}

function reload(){
   location.reload();
}