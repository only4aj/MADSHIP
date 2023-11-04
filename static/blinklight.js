// Set Blink blue light in my Cart function
function blink() {
  let dotbox = document.getElementById("dotbox");

  if (localStorage.length >= 1) {
    dotbox.innerHTML = `<div class="dot" id="dot" style="width: 15px; height: 15px; background: blue; border-radius: 50%;"></div>`;
    dotbox.style = `position: absolute;
    right: 45px;
    top: 5px;`;
  }
  if (!localStorage.length) {
    let dot = document.getElementById("dot");
    dot.remove();
  }
}


// .dotbox {
    // position: absolute;
    // right: 45px;
    // top: 5px;
// }

// .dot{
    // width: 15px;
    // height: 15px;
    // background: blue;
    // border-radius: 50%;
// }
