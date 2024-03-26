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
    const NAME = document.getElementById("block-name");
    const NAMEPLACEHOLDER = document.getElementById("block-name-placeholder");
    const DESC = document.getElementById("block-desc");
    const DESCPLACEHOLDER = document.getElementById("block-desc-placeholder");

    let blockDesc = e.target.getAttribute("alt");
    let blockName = e.target.getAttribute("id").split("-");

    // capitalize blockName words
    blockName = blockName.map((word) => {
      return word[0].toUpperCase() + word.substr(1);
    });

    let blockColor =
      "#" + JSON.parse(e.target.getAttribute("data-maphilight"))["strokeColor"];

    NAME.innerText = blockName.join(" ");
    NAME.style.color = blockColor;
    NAMEPLACEHOLDER.innerText = " in ";

    DESC.innerText = blockDesc;
    DESC.style.color = blockColor;
    DESCPLACEHOLDER.innerText = "";
  }
}

function resetBlockLabel(e) {
  if (e.target.getAttribute("id") === "game-board-image") {
    const NAME = document.getElementById("block-name");
    const NAMEPLACEHOLDER = document.getElementById("block-name-placeholder");
    const DESC = document.getElementById("block-desc");
    const DESCPLACEHOLDER = document.getElementById("block-desc-placeholder");

    NAME.innerText = "";
    NAMEPLACEHOLDER.innerText = ". . .";

    DESC.innerText = "";
    DESCPLACEHOLDER.innerText = "Click on a block to learn more!";
  }
}

window.addEventListener("resize", setupBlockAreas);
document.addEventListener("DOMContentLoaded", setupBlockAreas);
document.addEventListener("mouseover", setBlockLabel);
document.addEventListener("mouseout", resetBlockLabel);
