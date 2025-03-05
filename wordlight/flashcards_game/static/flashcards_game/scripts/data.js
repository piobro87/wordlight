function getSetName() {
    let path = location.pathname;
    let directories = path.split("/");
    let setName = directories[(directories.length - 2)];

    return setName;
}


async function getCardsFromCategory() {
    let setName = getSetName()
    let response = await fetch(`/api/flashcards/${setName}`);
    let cards = await response.json()

    return cards;
}

export {getCardsFromCategory, getSetName}
