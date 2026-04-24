"use strict";

const orderChanger = document.getElementById("order-changer");
const appearances = document.getElementById("appearances");

orderChanger.onchange = (event) => {
  const appearancesList = appearances.querySelectorAll("li");
  const reversedList = Array.from(appearancesList).reverse();
  for (const item of reversedList) {
    appearances.appendChild(item);
  }
};