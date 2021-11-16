var botao = window.document.querySelector("input#botao")
botao.addEventListener('click', nacao)
function nacao() {
    var origem = String(window.document.querySelector("input#origem").value).toUpperCase()
    var resultado = window.document.querySelector("div#res")
    var nacionalidade = " "
    if(origem === "BRASIL") {
        nacionalidade = "Brasileiro"
    }else {
        nacionalidade = "Estrangeiro"
    }
    resultado.innerHTML = nacionalidade
}
