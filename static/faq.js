document.addEventListener("DOMContentLoaded", function() {
    const faqItems = document.querySelectorAll(".faq");

    faqItems.forEach(faq => {
        const question = faq.querySelector(".question");
        const answer = faq.querySelector(".answer");

        question.addEventListener("click", () => {
            faq.classList.toggle("active");
            answer.classList.toggle("active");
        });
    });
});
