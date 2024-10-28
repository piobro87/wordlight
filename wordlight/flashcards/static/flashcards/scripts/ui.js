import {openAddCardForm} from "./utils.js";
import {getAllCards, createCard, deleteCard, deleteAllCards} from "./data.js";

const showBtn = document.getElementById("show-btn");
const addContainer = document.getElementById("card-window");
const closeBtn = document.getElementById("close");
const questionFront = document.getElementById("question");
const answerBack = document.getElementById("answer");
const saveBtn = document.getElementById("save-card");
const errorMessage = document.querySelector(".error-message");
const cardWrapper = document.getElementById("card-list");
const clearBtn = document.getElementById("clear");
const search = document.getElementById("search");
const searchBtn = document.getElementById("search-btn");
const searchResults = document.getElementById("results");
const errorSearch = document.getElementById("error-search");


function closeAddForm() {
    addContainer.classList.remove("show");
}

showBtn.addEventListener("click", () => {
    openAddCardForm(addContainer, questionFront, errorMessage, answerBack);
});
closeBtn.addEventListener("click", () => {
    closeAddForm();
});


function createCardElement(card, onDelete) {
    let cardDOM = document.createElement("div");
    cardDOM.classList.add("card");
    cardDOM.innerHTML = `
  <div class="card-container">
  		<div class="inner-card-front">
			<h2 class="mb20">Question:</h2>
			<p class="card-front">
			${card.original_text}
			</p>
	 	</div>
	 	<div class="inner-card-back">
	 		<h2 class="mb20">Answer:</h2>
			<p class="card-back">
			${card.translated_text}
			</p>
  		</div>
		<div class="actions">
			<a href="#" id="delete" class="delete"><i class="far fa-trash-alt" id="remove-button"></i></a>
			<a href="#" id="flip"><i class="fas fa-redo-alt" id="flip-button"></i></a>
		</div>
	</div>
  `;

    cardDOM.addEventListener("click", () =>
        cardDOM.classList.toggle("show-answer")
    );


    cardDOM
        .getElementsByClassName("delete")[0]
        .addEventListener("click", onDelete);

    return cardDOM;
}


async function showCards(arr) {
    cardWrapper.innerHTML = "";
    arr.forEach((card) => {
        let cardDOM = createCardElement(card, async () => {
            await deleteCard(card.id);
            await showCards(await getAllCards());
        });
        cardWrapper.appendChild(cardDOM);
    });
}


saveBtn.addEventListener("click", async (e) => {
    e.preventDefault();
    let front = questionFront.value;
    let back = answerBack.value;
    if (front !== "" && back !== "") {
        await createCard(front, back);
        await showCards(await getAllCards());
    } else {
        errorMessage.style.display = "block";
    }
    closeAddForm();
});

clearBtn.addEventListener("click", async () => {
    await deleteAllCards();
    location.reload();
});


searchBtn.addEventListener("click", async () => {
    let searchValue = search.value;
    let searchArr = searchCard(searchValue);
    await showCards(searchArr);
    if (searchArr.length === 0) {
        alert("There are no similar words!");
    }
    search.value = "";
});

document.addEventListener("DOMContentLoaded", async () => {
    await showCards(await getAllCards());
});
