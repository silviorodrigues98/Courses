//General Functions/Variables
var btn1 = document.querySelector("#btn1")
var btn2 = document.querySelector("#btn2")
var cont = 0
var allNumbers = []
var firstSection = document.querySelector("#firstSection")
var divRes = document.querySelector("#divres")
var newDivOnSection = createNewElement("p")
newDivOnSection.setAttribute("id", "divres2")
var btnCleanAll = document.getElementById("btnCleanAll")
var slc1 = document.querySelector("#slc1")
btnCleanAll.addEventListener("click", () => {
    
})
//
function createNewElement(element) {
    var elementType = document.createElement(`${element}`)
    return elementType
}
function appendNewChild (parent, element, innerElement) {
    var child = createNewElement(`${element}`)
    child.innerHTML = innerElement
    parent.appendChild(child)
}
//Add Button Click Event
btn1.addEventListener("click", click1 = () => {
    var nbr1 = Number(document.querySelector("#nbr1").value)
    if(nbr1 != 0) {
        cont += 1
        var add = document.createElement("option")
        var opt1 = document.querySelector("#opt1")
        allNumbers.push(nbr1)
        if(cont == 1){
            slc1.innerHTML = " "
        }
        add.text = `Número ${nbr1} adicionado`
        slc1.appendChild(add)
    }else {
        window.alert(`[ERRO] Você tentou adicionar o número ${nbr1}`)
    }
})


//Hit Enter Keyboard to Submit
var inputField = document.querySelector("#nbr1")
inputField.addEventListener("keydown", function(event) {
    if(event.keyCode == 13) {
        click1()
    }

})

//Finish Buttom Click Event
btn2.addEventListener("click", () => {
    var nbr2 = Number(document.querySelector("#nbr1").value)
    if(nbr2 != 0) {
        divRes.appendChild(newDivOnSection)
        var divres2 = document.querySelector("#divres2")
        divres2.innerHTML = " "
        var totalValueOfNumbers = 0
        var maxNumber = allNumbers[0]
        var minNumber = allNumbers[0]
        for(c=0; c < allNumbers.length; c++) {
            totalValueOfNumbers += allNumbers[c]
            if(allNumbers[c] > maxNumber) {
                maxNumber = allNumbers[c]    
            }else if(allNumbers[c] < minNumber) {
                minNumber = allNumbers[c]
        }
    }

        averageValueOfNumbers = Math.floor(totalValueOfNumbers/cont)
        appendNewChild(divres2, "p", `Foram digitados ${cont} números.`)
        appendNewChild(divres2, "p", `A soma deles é: ${totalValueOfNumbers}`)
        appendNewChild(divres2, "p", `A média entre eles é: ${averageValueOfNumbers}`)
        appendNewChild(divres2, "p", `O maior foi ${maxNumber}`)
        appendNewChild(divres2, "p", `O menor foi ${minNumber}`)
        nbr1.focus()
}else{
    window.alert("[ERRO] Você precisa digitar um número diferente de 0")
}
})

//Clean All Data Button
var btnCleanAll = document.querySelector("#btnCleanAll")
btnCleanAll.addEventListener("click", () => {
    slc1.innerHTML = " "
    divres2.innerHTML = " "
    cont = 0
    allNumbers = []
    var newOption = document.createElement("option")
    newOption.innerHTML = "Seus números aparecerão aqui:"
    slc1.appendChild(newOption)
    nbr1.focus()
})