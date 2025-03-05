import {getCardsFromCategory, getSetName} from "./data.js";

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

function getAnswers() {
    // Get all elements with class "card-container"
    const cardContainers = document.querySelectorAll(".card-container");

    // Initialize an array to hold the answers
    const answers = [];

    // Iterate over each card-container and retrieve input values
    cardContainers.forEach((container) => {
        const input = container.querySelector(".card-input"); // Find the input inside the container
        if (input) {
            answers.push({
                id: input.id, // Get the ID of the input
                answer: input.value.trim() // Get the input value
            });
        }
    });

    return answers;
}

async function sendAnswers() {
    let answers = getAnswers();
    let data = {
        "category": getSetName(),
        "answers": answers
    }
    let response = await fetch(`/api/flashcard-check/`, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {"Content-Type": "application/json", 'X-CSRFToken': getCookie("csrftoken")}
    });

    let answersResult = await response.json();
    return answersResult;
}

function changeFeedbackColours(answersResult) {
    for (const [key, value] of Object.entries(answersResult)) {
        const inputs = document.querySelectorAll(`input[id="${key}"]`);
        console.log(inputs);
        inputs.forEach((input) => {
           if(value === true){
               input.style.backgroundColor = "lightgreen";
           }
           else {
                input.style.backgroundColor = "lightcoral";
           }
        });
    }
}

document.addEventListener("DOMContentLoaded", async () => {
    await showCards(await getCardsFromCategory());
});

submitBtn.addEventListener("click", async () => {
    let answersResult = await sendAnswers();
    changeFeedbackColours(answersResult);
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
