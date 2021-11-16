var velocidade = 80 //Velocidade do veículo análisado.
var permitida = 70 //Limite máximo de velocidade da via.
var margem = 1.1 //Margem de erro permitida por via.

console.log(`A velocidade é ${velocidade} km/h`)
if(velocidade > (permitida*margem)) {
    console.log(`Você ultrapassou a velocidade permitida de ${permitida} km/h. MULTADO!`)
}else {
    console.log('Parabéns, você está respeitando as LEIS ESTATAIS !!!')
}

var pais = 'Estados Unidos'

if(pais=="Brasil") {
    var nacionalidade = 'Brasileiro'
}else {
    var nacionalidade = 'Estrangeiro'
}
console.log(`O cidadão em questão vive no ${pais} e é ${nacionalidade}`)

//Apertar F8 para executar o código (como se fosse Python)