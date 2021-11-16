var idade = 67
console.log(`Você tem ${idade} anos
Sua situação é: `)
if(idade < 16) {
    console.log('Não vota')
}else if (idade < 18 || idade > 65) {
    console.log('Voto opcional')
}else {
    console.log('Obrigado a votar')
}

var hora = new Date()
var agora = hora.getHours()
console.log(`Agora são exatamente ${hora} horas`)
if(hora <= 12) {
    console.log('Bom dia !')
}else if(hora <= 18) {
    console.log('Boa tarde !')
}else {
    console.log("Boa noite !")
}

var agora = new Date()
var dia = agora.getDay()
var escrito = " "
switch(dia) {
    case 0:
        escrito = "Domingo"
        break
    case 1:
        escrito  = "Segunda"
        break
    case 2:
        escrito = "Terça"
        break
    case 3:
        escrito = "Quarta"
        break
    case 4:
        escrito = "Quinta"
    case 5:
        escrito = "Sexta"
        break
    case 6:
        escrito = "Sábado"
        break
    defaut:
        escrito = "Erro"
        break
}
console.log(`Hoje é ${escrito}`)