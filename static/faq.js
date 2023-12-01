document.addEventListener("DOMContentLoaded", function () {
  const faqItems = document.querySelectorAll(".faq");

  faqItems.forEach((faq) => {
    const question = faq.querySelector(".question");
    const answer = faq.querySelector(".answer");

    question.addEventListener("click", () => {
      faq.classList.toggle("active");
      answer.classList.toggle("active");
    });
  });
});

function change(id) {
  if(document.querySelector("#"+id).classList.contains("fa-chevron-up")){
    document.querySelector("#"+id).classList.remove("fa-chevron-up");
    document.querySelector("#"+id).classList.add("fa-chevron-down");
  }
  else if(document.querySelector("#"+id).classList.contains("fa-chevron-down")){
    document.querySelector("#"+id).classList.remove("fa-chevron-down");
    document.querySelector("#"+id).classList.add("fa-chevron-up");
  }
}

// setInterval(function(){
//     console.log(window.innerWidth)
// // },1000)
// function resize(){
//   console.log(window.innerWidth)
// //   console.log(typeof(window.innerWidth))
// //   // console.log(document.getElementById("navbaar"))
//   if (window.innerWidth <= 767){
//     document.getElementById("navbaar").innerHTML = ''
//     document.getElementById("username").style = `position: absolute;
//     right: 75px;`
//   }
//   else{
//     document.getElementById("profile").innerHTML = `<li><a href="{% url 'home' %}">Home</a></li>
//     <li><a href="{% url 'store' %}">Store</a></li>
//     <li><a href="{% url 'about' %}">About Us</a></li>
//     <li><a href="{% url 'contact' %}">Contact Us</a></li>
//     <li><a href="{% url 'logout' %}">Logout</a></li>`
//     document.getElementById("username").style = `position: none;
//     right: 0;`
//   }
// }