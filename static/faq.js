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
  if (document.getElementsByClassName("fa-chevron-up").length > 0) {
    document.querySelector("#"+id).classList.toggle("fa-chevron-down");
    document.querySelector("#"+id).classList.remove("fa-chevron-up");
  } else if (document.getElementsByClassName("fa-chevron-down").length > 0) {
    document.querySelector("#"+id).classList.remove("fa-chevron-down");
    document.querySelector("#"+id).classList.toggle("fa-chevron-up");
  }
}
