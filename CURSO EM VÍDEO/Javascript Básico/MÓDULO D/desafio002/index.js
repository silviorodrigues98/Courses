
var msg = window.document.getElementById('msg')
var img = window.document.getElementById('imagem')
var data = new Date()
var hora = data.getHours()
msg.innerHTML = `<strong>Agora são ${hora} horas.</strong>`

if(hora < 12 && hora > 0) {
    img.src = "img/manha.jpg"
    document.body.style.background = 'orange'
}else if(hora <= 18){
    img.src = "img/tarde.jpg"
    document.body.style.background = 'yellow'
}else{
    img.src = 'img/noite.jpg'
    document.body.style.background = 'blue'
}