const header = document.querySelector("header");
const uptadeHeader = document.getElementById("update_header");

uptadeHeader.addEventListener("click", function() {
    header.textContent = "New Header!!!";
})
