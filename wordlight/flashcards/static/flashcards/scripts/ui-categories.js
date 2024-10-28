import { openAddCategoryForm } from './utils.js'

const showBtnCategory = document.getElementById("show-btn-category")
const addContainer = document.getElementById("card-window");
const saveBtn = document.getElementById("save-category");
const categoryFront = document.getElementById("category-name");
const errorMessage = document.querySelector(".error-message");

function closeAddForm() {
  addContainer.classList.remove("show");
}

showBtnCategory.addEventListener("click", () => {
    openAddCategoryForm(addContainer);
});


saveBtn.addEventListener("click", async (e) => {
  e.preventDefault();
  let categoryName = categoryFront.value;

  if (categoryName !== "") {
    await createCategory(categoryName);
    closeAddForm();
  } else {
    errorMessage.style.display = "block";
  }
});


async function createCategory(categoryName) {

    let category = { set_name: String(categoryName), language_variation: 1 };
    let categoryJSON = JSON.stringify(category);

    let response = await fetch(`/api/flashcard-set/`, {
        method: "POST",
        body: categoryJSON,
        headers: {"Content-Type": "application/json", 'X-CSRFToken': getCookie("csrftoken")}

    });

    if (response.status == 201) {
        return category;
    }
}
