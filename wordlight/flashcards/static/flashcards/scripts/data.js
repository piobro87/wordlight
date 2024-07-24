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

function setCookie(name, value, days) {
  let expires = "";
  if (days) {
    let date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
  let nameEQ = name + "=";
  let ca = document.cookie.split(';');
  for(let i=0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

function eraseCookie(name) {
  document.cookie = name + '=; Max-Age=-99999999;';
}

function createCard(front, back) {
  let card = { id: currentIdCard, front: String(front), back: String(back) };
  let cardJSON = JSON.stringify(card);
  setCookie(card.id, cardJSON, 365); // setting the cookie to expire in 365 days
  currentIdCard++; // increase card's id every time when func calls
  return card;
}

function deleteCard(id) {
  eraseCookie(id);
}

function searchCard(query) {
  let cards = getAllCards();
  return cards.filter(card => card.front.includes(query) || card.back.includes(query));
}

function deleteAllCards() {
  let cookies = document.cookie.split(';');
  cookies.forEach(cookie => {
    let [key] = cookie.split('=');
    key = key.trim();
    if (!isNaN(key)) { // ensuring the key is a number, indicating a card
      eraseCookie(key);
    }
  });
}

function getAllCards() {
  // TODO Implement communication with API for retrieving cards
  // /card/<string:category>/get-all/
  //

  let cookies = document.cookie.split(';');
  let cards = [];
  cookies.forEach(cookie => {
    let [key, value] = cookie.split('=');
    key = key.trim();
    if (!isNaN(key)) { // ensuring the key is a number, indicating a card
      cards.push(JSON.parse(decodeURIComponent(value)));
    }
  });
  return cards;
}
