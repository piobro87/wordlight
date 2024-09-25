/*
Data view

Card structure:
{
	id: 0,
	front: "Question",
	back: "Answer"
}
*/

let currentIdCard = 0;

async function createCard(front, back) {
    let setName = getSetName()
    let card = {original_text: String(front), translated_text: String(back), set_name: String(setName) };
    let cardJSON = JSON.stringify(card);

    let response = await fetch(`/api/flashcard/`, {
        method: "POST",
        body: cardJSON,
        headers: {"Content-Type": "application/json", 'X-CSRFToken': getCookie("csrftoken")}
    });

    if (response.status == 201) {

        return card;
    }
}

async function deleteCard(id) {
    let response = await fetch(`/api/flashcard/${id}`, {
        method: "DELETE",
        headers: {"Content-Type": "application/json", 'X-CSRFToken': getCookie("csrftoken")}
    });
}

function searchCard(query) {
    let cards = getAllCards();
    return cards.filter(card => card.front.includes(query) || card.back.includes(query));
}

async function deleteAllCards() {
    let setName = getSetName()
    let response = await fetch(`/api/flashcards/${setName}`, {method: "DELETE",
        headers: {"Content-Type": "application/json", 'X-CSRFToken': getCookie("csrftoken")}
    });
}

async function getAllCards() {
    let setName = getSetName()
    let response = await fetch(`/api/flashcards/${setName}`);
    let cards = await response.json()

    return cards;
}


function getSetName() {
    let path = location.pathname;
    let directories = path.split("/");
    let setName = directories[(directories.length - 2)];

    return setName;
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
