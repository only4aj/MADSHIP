// Set Blink blue light in my Cart function

let num = 0;
for (let i = 0; i < localStorage.length; i++) {
  if (Number(localStorage.key(i))) {
    num++;
  }
}

if(num == 0){
  document.getElementById("dot").remove()
}

function blink() {
  let dotbox = document.getElementById("dotbox");

  if(num == 0){
    location.reload()
  }
  if (num == 1) {
    dotbox.innerHTML = `<div class="dot" id="dot"></div>`;
  }
  else if (!num) {
    document.getElementById("dot").remove();
  }
}

// .dotbox {
//     position: absolute;
//     right: 45px;
//     top: 5px;
// }

// .dot{
//     width: 15px;
//     height: 15px;
//     background: blue;
//     border-radius: 50%;
// }
