var num = [5, 8, 1]
console.log(num)
num[3] = 6 // Faz o num receber, como se fosse um append.
num.push(7) // ESTE É IGUAL APPEND, ADICIONANDO O VALOR NO FINAL DO ARRAY.
console.log(num.length) // Retorna o tamanho.
num.sort() // Coloca eles em ordem crescente.
console.log(num)
console.log(num[2]) // Mostra o valor na posição 2 do array.
// for(let pos = 0; pos < num.length; pos++) {
//     console.log(num[c]) // É uma forma de printar o array sem a formatação padrão.
// } // Percurso em vetores.
// Jeito fácil do JS(SÓ JS)
for(let pos1 in num) {
    console.log(num[pos1])
} //Este formato existe só no JS, mas é mais simples, funciona somente em arrays ou objects.

//É posivel buscar posição de algo dentro do ARRAY.

console.log(num.indexOf(7))// Mostra a posição do número 7.