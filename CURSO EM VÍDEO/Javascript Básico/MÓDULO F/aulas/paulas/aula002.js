/* Funções em JS 
Elas facilitam ações repetitivas.
Toda função tem que ter uma chamada, dizendo quando será ativada.
Além disso. elas também precisam de parâmetros.
E o que acontece lá dentro é chamada de ação.
Finalmente, elas retornam algo.
função ação(param) {
    ação programada
    retorno
}
ação(5)*/ 

function parimp(n) {
    if(n%2===0){
        return "par"
    }else{
        return "ímpar"
    }
}
let res = parimp(11)
console.log(`seu número é ${res}`)

function soma(n1= 1, n2= 1) {
    return n1+n2
}
var som = soma(1, 3)
console.log(som)

var x = function(x) {
    return x
}

function fatorial(n) { //Recursividade
    if(n == 1){
        return 1
    }else {
        return n * fatorial(n-1)
    }
}
console.log(fatorial(5))