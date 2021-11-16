var click = document.querySelector("#btn1")
click.addEventListener("click", clicar)
function clicar () {

    var ini = Number(document.querySelector("#txt1").value)
    var fim = Number(document.querySelector("#txt2").value)
    var passo = Number(document.querySelector("#txt3").value)
    var res = document.querySelector("#res")
    if(passo === 0) {
        passo = 1
        window.alert('Passo inválido! Padrão a ser utilizado será (UM)[1]')
    }else if(passo < 0) {
        passo *= -1
        }
    res.innerHTML = `Contando de ${ini} até ${fim}, de ${passo} em ${passo}:<br>`
    function contar() {
        return res.innerHTML += `${c} \u{1F449}`
    }
    if(ini == 0 && fim == 0) {
        window.alert("[ERRO] Faltam dados! ")
        
    }else{

        if(ini > fim) {

            for(c = ini; c >= fim; c -= passo) {
                contar()
            }
        }else {
            for(c = ini; c <= fim; c += passo) {
                contar()
            }
        }

    res.innerHTML += `\u{1F3C1} FIM !!!`
}
}
