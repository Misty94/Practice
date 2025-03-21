const image = document.querySelector(".image");
const img1 = document.querySelector(".img1");
const layer = document.querySelector(".layer");
const circle = document.querySelector(".circle");

var condition = false;
circle.addEventListener("mousedown", () => condition = true);
window.addEventListener("mouseup", () => condition = false);
layer.addEventListener("mousemove", (ev) => {
    if (condition) {
        let width = (ev.clientX - image.offsetLeft) + "px";
        img1.style.width = width;
        circle.style.left = width;
    }
})