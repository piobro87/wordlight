import { getAllCards } from "./data.js";

const cardWrapper = document.getElementById("card-list");

async function showCards(arr) {
  cardWrapper.innerHTML = "";
  arr.forEach((card) => {
    let cardDOM = createCardElement(card, async () => {
      await showCards(await getAllCards());
    });
    cardWrapper.appendChild(cardDOM);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
    await showCards(await getAllCards());
});
