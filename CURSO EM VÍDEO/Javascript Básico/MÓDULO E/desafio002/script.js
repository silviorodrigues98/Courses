var btn1 = document.querySelector("#btn1")
btn1.addEventListener("click", click1 = () => {
    let nbr1 = Number(document.querySelector("#nbr1").value)
    let slc1 = document.querySelector("#slc1")
    slc1.innerHTML = " "
    if(nbr1 === 0) {
        window.alert("[ERRO] Você não digitou nenhum número!")
    }else {
        let count = 1
        while(count <= 10) {
            let item = document.createElement("option")
            item.text = `${nbr1} x ${count} = <strong>${nbr1*count}</strong>`
            slc1.appendChild(item)
            count += 1
            item.value = `tab${count}`
        }
    }
})