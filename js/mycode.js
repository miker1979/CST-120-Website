document.addEventListener("DOMContentLoaded", function () {
  console.log("JS Loaded");

  const title = document.getElementById("title");

  if (title) {
    title.addEventListener("click", function () {
      alert("This is fun!");
    });
  }
});

function sayHello() {
  alert("Hello world!");

  const helloText = document.getElementById("hello-text");
  if (helloText) {
    helloText.innerHTML = "Hello world!";
  }

  console.log("Hello world!");

  let age = 45;
  let name = "Mike";

  console.log(`My name is ${name}`);
  console.log(`My age is ${age}`);
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

function displayArray(value, index) {
  console.log(`Array value: ${value} at index ${index}`);
}

// =========================
// CONDITIONS
// =========================

function conditions() {
  let num1 = 10;
  let num2 = 5;

  if (num1 === num2) {
    console.log("Equal");
  } else {
    console.log("Not equal");
  }
}

// =========================
// LOOPS
// =========================

function loops() {
  let shapes = ["Triangle", "Circle", "Square"];

  for (let i = 0; i < shapes.length; i++) {
    console.log(shapes[i]);
  }
}

// =========================
// OBJECTS
// =========================

function objects() {
  function Person(firstName, lastName, age, occupation) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.occupation = occupation;

    this.display = function () {
      console.log(`${this.firstName} ${this.lastName} - ${this.occupation}`);
    };
  }

  let person = new Person("Mike", "Robinson", 45, "Developer");
  person.display();
}