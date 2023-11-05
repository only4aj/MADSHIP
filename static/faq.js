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
