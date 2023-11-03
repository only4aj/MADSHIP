
let qty = 1;
function setdata() {
    let title = document.getElementById("ttl").textContent
    let image = document.getElementById("imgg").src
    let price = Number(document.getElementById('price').textContent)
    let actprc = Number(document.getElementById('act').textContent)
    let id = document.getElementById('id').textContent

    for (let i = 0; i < localStorage.length; i++) {
        if (localStorage.key(i) == id) {
            qty = Number(JSON.parse(localStorage.getItem(localStorage.key(i))).quantity) + 1
            localStorage.removeItem(id)
            data = {
                'title': title,
                "quantity": qty,
                "image": image,
                "price": price,
                "actprc": actprc
            }
            data = JSON.stringify(data)
            localStorage.setItem(id, data)
        }
    }
    data = {
        'title': title,
        "quantity": qty,
        "image": image,
        "price": price,
        "actprc": actprc
    }
    data = JSON.stringify(data)
    localStorage.setItem(id, data)
}