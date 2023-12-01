let qty = 1;
let num = 0;
for (let i = 0; i < localStorage.length; i++) {
    if (Number(localStorage.key(i))) {
        num++;
    }
}
let dot = document.getElementById("dot");
if (num == 0) {
  dot.remove();
}

// Update Quantity Function
function setdata() {
  let title = document.getElementById("ttl").textContent;
  let image = document.getElementById("imgg").src;
  let price = Number(document.getElementById("price").textContent);
  let actprc = Number(document.getElementById("act").textContent);
  let id = document.getElementById("id").textContent;

  for (let i = 0; i < localStorage.length; i++) {
    if (Number(localStorage.key(i)) == id) {
      qty = Number(JSON.parse(localStorage.getItem(localStorage.key(i))).quantity) +1;
      localStorage.removeItem(id);
      data = {
        title: title,
        quantity: qty,
        image: image,
        price: price,
        actprc: actprc,
      };
      data = JSON.stringify(data);
      localStorage.setItem(id, data);
    }
  }
  data = {
    title: title,
    quantity: qty,
    image: image,
    price: price,
    actprc: actprc,
  };
  data = JSON.stringify(data);
  localStorage.setItem(id, data);
}


// Set Blink blue light in my Cart function
function blink() {
  if(num == 0){
    location.reload()
  }
  let dotbox = document.getElementById("dotbox");
  if (num == 1) {
    dotbox.innerHTML = `<div class="dot" id="dot"></div>`;
  }
  else if (!num) {
    let dot = document.getElementById("dot");
    dot.remove();
  }

  if (num > 0) {
    let dot = document.getElementById("dot");
    dot.style = `box-shadow: 0 0 5px rgb(244, 179, 179), 0 0 8px #f75858, 0 0 10px red, 0 0 15px darkred,0 0 20px rgb(248, 154, 154);`;
    setTimeout(function () {
      dot.style = `box-shadow: none;`;
    }, 100);
  }
}
