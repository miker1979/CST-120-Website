document.addEventListener("DOMContentLoaded", function () {
  console.log("Playground JS Loaded");

  const title = document.getElementById("title");

  if (title) {
    title.addEventListener("click", function () {
      alert("This is fun!");
    });
  }
});

// =========================
// SIMPLE DEMOS (ONLY RUN WHEN CALLED)
// =========================

function sayHello() {
  alert("Hello world!");

  const el = document.getElementById("hello-text");
  if (el) {
    el.innerHTML = "Hello world!";
  }
}

// =========================
// REUSABLE FUNCTIONS
// =========================

function add(num1, num2) {
  return num1 + num2;
}

function multiply(num1, num2) {
  return num1 * num2;
}

// =========================
// DEMO RUNNERS (ONLY WHEN BUTTON CLICKED)
// =========================

function runConditions() {
  console.clear();
  console.log("CONDITIONS");

  let num1 = 10;
  let num2 = 5;

  console.log(num1 === num2 ? "Equal" : "Not Equal");
}

function runLoops() {
  console.clear();
  console.log("LOOPS");

  let shapes = ["Triangle", "Circle", "Square"];

  shapes.forEach(shape => console.log(shape));
}

function runObjects() {
  console.clear();
  console.log("OBJECTS");

  function Person(name, age) {
    this.name = name;
    this.age = age;
  }

  let p = new Person("Mike", 45);
  console.log(p);
}