import { openAddCategoryForm } from './utils.js'

const showBtnCategory = document.getElementById("show-btn-category")
const addContainer = document.getElementById("card-window");

showBtnCategory.addEventListener("click", () => {
    openAddCategoryForm(addContainer);
});
