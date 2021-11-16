let amigo = {nome:"José", idade:25, sexo:"M", peso:10, engordar(p=0){
    this.peso += p
}}
console.log(`${amigo.nome} pesava ${amigo.peso} kg.`)
amigo.engordar(10)
console.log(`${amigo.nome} agora pesa ${amigo.peso} kg`)
//Isto acontece pois ativei a função dentro do objeto. 