var btn1 = document.querySelector("input#btn1")
btn1.addEventListener("click", verificar)

function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById("txtano")
    var res = document.getElementById("res")
    if(fano.value.length == 0 || fano.value >= ano) { //alt+124
        window.alert('ERRO! VERIFIQUE OS DADOS E TENTE NOVAMENTE !')
    }else {
        var fsex = document.getElementsByName("radsex") //[0] ou [1]
        var idade= ano - Number(fano.value)
        var genero = "#"
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if(fsex[0].checked) {
            genero = "Homem"
            if(idade <= 3) {
                img.setAttribute("src", "img/bebe-homem.jpg")
            }else if(idade <=13) {
                img.setAttribute("src", "img/crianca-homem.jpg")
            }else if(idade <= 30) {
                img.setAttribute("src", "img/jovem-homem.jpg")
            }else if(idade < 60) {
                img.setAttribute("src", "img/adulto-homem.jpg")
            }else {
                img.setAttribute("src", "img/velho-homem.jpg")
            }

        }else {
            genero = "Mulher"
            if(idade <= 3) {
                img.setAttribute("src", "img/bebe-mulher.jpg")
            }else if(idade <=13) {
                img.setAttribute("src", "img/crianca-mulher.jpg")
            }else if(idade <= 30) {
                img.setAttribute("src", "img/jovem-mulher.jpg")
            }else if(idade < 60) {
                img.setAttribute("src", "img/adulto-mulher.jpg")
            }else {
                img.setAttribute("src", "img/velho-mulher.jpg")
            }
        }
            


    res.style.textAlign = 'center' //Alinha sem usar o CSS
    res.innerHTML = `Detectamos o gênero <strong>${genero}</strong> com <strong>${idade}</strong> anos.`
    res.appendChild(img)   
    }
}