const ALPHABET = "abcdefghijklmnopqrstuvwxyz";
const WORDS = [
  "strawberry",
  "orange",
  "apple",
  "banana",
  "pineapple",
  "kiwi",
  "peach",
  "pecan",
  "eggplant",
  "durian",
  "peanut",
  "chocolate",
];

let numWrong = 0;
let correctGuess = 0;

// Loop over the chars in `word` and create divs.
//

const createDivsForChars = (word) => {
  const wordContainer = document.querySelector("#word-container");
  for (const letter of word) {
    wordContainer.insertAdjacentHTML(
      "beforeend",
      `<div class="letter-box ${letter}"></div>`
    );
  }
};

// Loop over each letter in `ALPHABET` and generate buttons.
//
const generateLetterButtons = () => {
  const letterButtonContainer = document.querySelector("#letter-buttons");
  for (const char of ALPHABET) {
    letterButtonContainer.insertAdjacentHTML(
      "beforeend",
      `<button>${char}</button>`
    );
  }
};

// Set the `disabled` property of `buttonEl` to `true.
//
// `buttonEl` is an `HTMLElement` object.
//
const disableLetterButton = (buttonEl) => {
  buttonEl.disabled = true;
};

const disableAllButtons = () => {
  const buttonDiv = document.querySelectorAll("button");
  console.log(buttonDiv);
  for (button of buttonDiv) {
    button.disabled = true;
  }
};
// Return `true` if `letter` is in the word.
//
const isLetterInWord = (letter) =>
  document.querySelector(`div.${letter}`) !== null;

// Called when `letter` is in word. Update contents of divs with `letter`.
//
const handleCorrectGuess = (letter) => {
  const selected_letter = document.querySelectorAll(`div.${letter}`);
  console.log(selected_letter);
  console.log(letter);
  for (div of selected_letter) {
    div.innerHTML = letter;
  }
  // Replace this with your code
};

//
// Called when `letter` is not in word.
//
// Increment `numWrong` and update the shark image.
// If the shark gets the person (5 wrong guesses), disable
// all buttons and show the "play again" message.

const handleWrongGuess = () => {
  numWrong += 1;
  console.log(numWrong);
  document
    .querySelector("img")
    .setAttribute("src", `/static/images/guess${numWrong}.png`);
  if (numWrong == 5) {
    disableAllButtons();
    document.querySelector("#play-again").style.display = "block";
  }
  // Replace this with your code
};

//  Reset game state. Called before restarting the game.
const resetGame = () => {
  window.location = "/sharkwords";
};

// This is like if __name__ == '__main__' in Python
//
(function startGame() {
  // For now, we'll hardcode the word that the user has to guess.
  const word = "hello";
  const word_set = new Set(word);
  console.log(word_set);
  createDivsForChars(word);
  generateLetterButtons();

  const buttons = document.querySelectorAll("button");
  const some_list = new Set();
  for (button of buttons) {
    button.addEventListener("click", (evt) => {
      const letter = evt.target.innerHTML;
      if (isLetterInWord(letter)) {
        console.log(letter);
        some_list.add(letter);
        console.log(some_list.size);
        if (some_list.size == word_set.size) {
          document.querySelector("#win").style.display = "block";
          disableAllButtons();
        }
        handleCorrectGuess(letter);
        disableLetterButton(evt.target);
        // let finished_word = document.querySelector("#word-container").innerHTML
        // console.log(finished_word)
        // for (letter of finished_word){
        //   console.log(letter.html)
        // }
      } else {
        handleWrongGuess();
      }
    });
  }

  // add an event handler to handle clicking on the Play Again button
  // YOUR CODE HERE
})();
