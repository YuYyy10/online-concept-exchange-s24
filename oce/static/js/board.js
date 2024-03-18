/*
500 pixels was the original image size when the block
areas were defined.

The original area coords are stored here because if only the
most recent area coords are rescaled repeatedly, rounding
error will accumulate and deform the areas.
*/
const ORIGINALWIDTH = 500;
const ORIGINALCOORDS = (() => {
  let temp = {};

  document.querySelectorAll("area").forEach((area) => {
    temp[area.getAttribute("id")] = area.getAttribute("coords");
  });

  return temp;
})();

function setupBlockAreas() {
  // as the parent element of the game board changes,
  // adjust the size of the image
  let wrapperWidth = document.querySelector("#map-wrapper").clientWidth;

  let boardImage = document.querySelector("#game-board-image");
  boardImage.setAttribute("width", parseInt(wrapperWidth));
  boardImage.setAttribute("height", parseInt(wrapperWidth));

  // adjust the size of the map areas to match the image
  resizeBlockAreas();

  // adjust the size of the canvas over the map
  $(function () {
    $(".map").maphilight({
      strokeWidth: Math.round(wrapperWidth / 100),
    });
  });
}

function resizeBlockAreas() {
  let newWidth = document
    .querySelector("#game-board-image")
    .getAttribute("width");

  document.querySelectorAll("area").forEach((area) => {
    // grab the coords and convert the string to an array of nums
    let newCoords = ORIGINALCOORDS[area.getAttribute("id")]
      .split(",")
      .map((num) => {
        return parseInt(num);
      });

    // rescale the coords
    newCoords = newCoords.map((num) => {
      return Math.round(num * ((newWidth * 1.0) / ORIGINALWIDTH));
    });

    area.setAttribute("coords", newCoords.join(","));
  });
}

function setBlockLabel(e) {
  if (
    e.target.tagName.toLowerCase() === "area" &&
    e.target.parentElement.getAttribute("name") === "game-board-map"
  ) {
    placeholder = document.getElementById("block-label-placeholder");
    label = document.getElementById("block-label");

    // the mouse has moved into a block: set label and placeholder
    words = e.target.getAttribute("id").split("-");

    // capitalize words
    words = words.map((word) => {
      return word[0].toUpperCase() + word.substr(1);
    });

    // for IDs with 3 words like "block-1-environment",
    // join the first 2 words with a space
    words = words.length >= 3 ? [words.slice(0, 2).join(" "), words[2]] : words;

    label.innerText = words.join(": ");
    label.style.color =
      "#" + JSON.parse(e.target.getAttribute("data-maphilight"))["strokeColor"];

    document.getElementById("block-label-placeholder").innerText =
      "Click to learn about ";
  }
}

function resetBlockLabel(e) {
  if (e.target.getAttribute("id") === "game-board-image") {
    placeholder = document.getElementById("block-label-placeholder");
    label = document.getElementById("block-label");

    placeholder.innerText = "Click on a block to learn more!";
    label.innerText = "";
  }
}

window.addEventListener("resize", setupBlockAreas);
document.addEventListener("DOMContentLoaded", setupBlockAreas);
document.addEventListener("mouseover", setBlockLabel);
document.addEventListener("mouseout", resetBlockLabel);
