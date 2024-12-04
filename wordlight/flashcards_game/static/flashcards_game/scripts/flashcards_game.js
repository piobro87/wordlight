import {getCardsFromCategory} from "./data.js";

const cardWrapper = document.getElementById("card-list");
const submitBtn = document.getElementById("show-btn");

async function showCards(arr) {
    cardWrapper.innerHTML = "";
    arr.forEach((card) => {
        let cardDOM = createCardElement(card);
        cardWrapper.appendChild(cardDOM);
    });
}

function createCardElement(card) {
    console.log(card);
    let cardDOM = document.createElement("div");
    cardDOM.classList.add("card-item");
    cardDOM.innerHTML = `
      <div class="card-container">
          <div class="inner-card-front">
              <h2 class="mb20">Translate:</h2>
              <p class="card-front">${card.original_text}</p>
          </div>
          <input id="${card.id}" type="text" class="card-input" placeholder="input">
      </div>
    `;

    return cardDOM;
}

function sendAnswers() {
    console.log("CALLED AFTER THE BUTTON CLICK");
}

document.addEventListener("DOMContentLoaded", async () => {
    await showCards(await getCardsFromCategory());
});

submitBtn.addEventListener("click", async () => {
    sendAnswers();
});
