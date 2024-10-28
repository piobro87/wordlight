async function getAllCards() {
    let setName = getSetName()
    let response = await fetch(`/api/flashcards/${setName}`);
    let cards = await response.json()

    return cards;
}

export { getAllCards }
