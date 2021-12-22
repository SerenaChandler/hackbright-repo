"use strict";
const color_button = document.querySelector(".color-changer");

color_button.addEventListener("click", () => {
  console.log("hello");
  const elements = document.querySelectorAll(".color-change");
  console.log(elements);
  for (const element of elements) {
    element.classList.add("class", "red");
  }
});

const input_form = document.querySelector(".number-form");

input_form.addEventListener("click", (event) => {
  event.preventDefault();
  const num_input = document.querySelector('#number-input').value;
  const feedback = document.querySelector("#formFeedback");
  console.log(num_input);
  if (parseInt(num_input) >= 10 || isNaN(num_input)) {
      feedback.textContent = "Please enter a smaller number";
  } else {
    feedback.innerHTML = "you are good to go!";
  }
});
