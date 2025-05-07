import {openAddCategoryForm} from './utils.js'
import {deleteCategory, getCookie} from "./data.js";

const showBtnCategory = document.getElementById("show-btn-category")
const addContainer = document.getElementById("card-window");
const saveBtn = document.getElementById("save-category");
const categoryFront = document.getElementById("category-name");
const errorMessage = document.querySelector(".error-message");

const modal = document.getElementById("share-modal");
const closeModal = document.querySelector(".close-modal");
const inviteBtn = document.getElementById("invite-btn");
const emailInput = document.getElementById("recipient-email");

let currentCategoryId = null;

function closeAddForm() {
    addContainer.classList.remove("show");
}

showBtnCategory.addEventListener("click", () => {
    openAddCategoryForm(addContainer);
});


saveBtn.addEventListener("click", async (e) => {
    e.preventDefault();
    let categoryName = categoryFront.value;

    const forbiddenChars = /[?#%/\\]/;
    if (forbiddenChars.test(categoryName)) {
        alert("Category name cannot contain special characters like: ?, #, %, /, \\");
        return;
    }

    if (categoryName !== "") {
        const result = await createCategory(categoryName);
        if (result) {
            closeAddForm();
            window.location.reload();
        }
    } else {
        errorMessage.style.display = "block";
    }
});


async function createCategory(categoryName) {

    let category = {set_name: String(categoryName), language_variation: 1};
    let categoryJSON = JSON.stringify(category);

    let response;
    response = await fetch(`/api/flashcard-set/`, {
        method: "POST",
        body: categoryJSON,
        headers: {"Content-Type": "application/json", 'X-CSRFToken': getCookie("csrftoken")}
    });

    if (response.status === 409) {
        alert("Such category already exists!");
        return null;
    }

    if (response.status === 201) {
        return category;
    }
}

document.querySelectorAll(".share-icon").forEach((icon, index) => {
    icon.addEventListener("click", () => {

        const categoryLink = document.querySelector(".rectangleFigure a");
        const categoryHref = categoryLink.getAttribute("href");
        const categoryId = categoryHref.split("/")[2];

        currentCategoryId = categoryId;
        modal.classList.remove("hidden");
    });
});

closeModal.addEventListener("click", () => {
    modal.classList.add("hidden");
});

inviteBtn.addEventListener("click", async () => {
    const recipient = emailInput.value;
    if (!recipient || !currentCategoryId) return;


    try {
        const res = await fetch('/api/flashcard-share/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                sharer: window.USER_ID,
                recipient: recipient,
                category_id: currentCategoryId
            })
        });

        const data = await res.json();
        alert(data.message);
        modal.classList.add("hidden");
    } catch (err) {
        console.error("Share failed", err);
    }
});


document.querySelectorAll(".trash-icon").forEach((icon) => {
    icon.addEventListener("click", async () => {
        const categoryCard = icon.closest(".categoryWrapper");
        const categoryLink = categoryCard.querySelector(".rectangleFigure a");
        const categoryHref = categoryLink.getAttribute("href");
        const categoryId = categoryHref.split("/")[2];

        await deleteCategory(categoryId);

        categoryCard.remove();
    });
});
