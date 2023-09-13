const header = document.querySelector("header")
const toggleHeader = document.getElementById("toggle_header")

toggleHeader.addEventListener("click", function(){
    const currentClass = header.classList;
    if (currentClass.contains("red")) {
        currentClass.remove("red");
        currentClass.add("green")
    } else {
        currentClass.remove("green");
        currentClass.add("red")
    }
})
