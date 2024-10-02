//Show add container block
function openAddCardForm(addContainer, questionFront, errorMessage, answerBack) {
  addContainer.classList.add("show");
  questionFront.value = "";
  errorMessage.style.display = "none";
  answerBack.value = "";
}

function openAddCategoryForm(addContainer) {
    addContainer.classList.add("show");
}

export { openAddCardForm, openAddCategoryForm }
