window.onload = initialize;

function initialize()
{
  console.log("In initialize()");

  document.getElementById("title").addEventListener("click", function () {
    alert("This is fun!");
  });
}



function sayHello()
{
  alert("Hello world!");
  document.getElementById("hello-text").innerHTML = "Hello world!";
  console.log("Hello world!");

  // =========================
  // VARIABLES and ASSIGNMENTS
  // =========================
  var age = 45;
  let name = "Mike";

  console.log("My name is " + name);
  console.log("My age is " + age);

  // =========================
  // MATH OPERATORS
  // =========================
  var number1 = 10;
  var number2 = 5;
  var result;

  result = number1 + number2;
  console.log("Addition result is " + result);

  result = number1 - number2;
  console.log("Subtraction result is " + result);

  result = number1 * number2;
  console.log("Multiplication result is " + result);

  result = number1 / number2;
  console.log("Division result is " + result);

  // =========================
  // INCREMENT / DECREMENT
  // =========================
  ++number1;
  console.log("Increment result is " + number1);

  --number1;
  console.log("Decrement result is " + number1);

  // =========================
  // EXPONENT
  // =========================
  result = number1 ** number2;
  console.log("Exponentiation result is " + result);

  // =========================
  // COMPARISON OPERATORS
  // =========================
  console.log("Equality for 10 is " + (number1 == 10));
  console.log("Equality for 2 numbers " + (number1 == number2));
  console.log("Equality for 2 numbers and type " + (number1 === number2));
  console.log("Inequality for 2 numbers " + (number1 != number2));
  console.log("Greater than for 2 numbers " + (number1 > number2));
  console.log("Less than for 2 numbers " + (number1 < number2));

  // =========================
  // STRINGS
  // =========================
  let string1 = 'A String enclosed in Single Quotes';
  console.log("String with single quotes: " + string1);

  let string2 = "A String enclosed in Double Quotes";
  console.log("String with double quotes: " + string2);

  let string3 = "A \"String\" which needs to be escaped";
  console.log("String with escaped quotes: " + string3);

  let string4 = "A string \n on two lines";
  console.log("String with newline: " + string4);

  // =========================
  // STRING METHODS
  // =========================
  let string5 = "Grand Canyon University";
  console.log("String length is " + string5.length);
  console.log("Upper case: " + string5.toUpperCase());
  console.log("Lower case: " + string5.toLowerCase());
  console.log("Index of Grand: " + string5.indexOf("Grand"));
  console.log("Index of Canyon: " + string5.indexOf("Canyon"));

  // =========================
  // NUMBERS
  // =========================
  let numberStr = "1";
  let numberNum = 1;

  console.log("numberStr type: " + typeof numberStr);
  console.log("numberNum type: " + typeof numberNum);

  console.log("Convert string to number: " + Number(numberStr));
  console.log("Convert number to string: " + numberNum.toString());
  console.log("Boolean to number: " + Number(false));
  console.log("Invalid number: " + Number("ABC"));

  console.log("Parse int: " + parseInt("10"));
  console.log("Parse float: " + parseFloat("10.53"));
  console.log("Random number: " + Math.random());

  // =========================
  // ARRAYS
  // =========================
  let shapes1 = ["Circle", "Square", "Triangle", "Rectangle"];

  console.log("First shape: " + shapes1[0]);
  console.log("Last shape: " + shapes1[shapes1.length - 1]);

  shapes1.sort();
  console.log("Sorted first: " + shapes1[0]);

  shapes1.reverse();
  console.log("Reversed first: " + shapes1[0]);

  shapes1.pop();
  console.log("After pop: " + shapes1);

  shapes1.push("Oval");
  console.log("After push: " + shapes1);

  for (let shape of shapes1)
  {
    console.log("Shape: " + shape);
  }

  // =========================
  // DATES
  // =========================
  let now = new Date();
  let birthday = new Date(1968, 9, 17, 0, 0, 0);

  console.log("Current date and time is " + now);
  console.log("Past date and time is " + birthday);
  console.log("Time difference is " + (now.getFullYear() - birthday.getFullYear()));

  // =========================
  // FUNCTION CALLS
  // =========================
  reusableCode();

  let result2 = add(15, 20);
  console.log("Result is " + result2);

  result2 = multiply(15, 20);
  console.log("Result is " + result2);

  shapes1.forEach(displayArray);
}


// =========================
// REUSABLE FUNCTIONS
// =========================

function reusableCode()
{
  console.log("Called the reusableCode() function");
}

function add(num1, num2)
{
  console.log("Adding numbers " + num1 + " and " + num2);
  return num1 + num2;
}

function multiply(num1, num2)
{
  console.log("Multiplying numbers " + num1 + " and " + num2);
  return num1 * num2;
}

function displayArray(value, index)
{
  console.log("From displayArray() the array value is " + value + " at " + index);
}

// If and Switch statements
function conditions()
{
  // Create some variables to compare
  let num1 = 10;
  let num2 = 5;
  let text1 = "Mike";
  let text2 = "Mary";

  // Do some comparisons with If statements using numbers
  if (num1 == num2)
    console.log("Number 1 is equal to Number 2");
  else
    console.log("Number 1 is not equal to Number 2");

  if (num2 > num1)
    console.log("Number 2 is greater than Number 1");
  else if (num2 < num1)
    console.log("Number 2 is less than Number 1");
  else
    console.log("Number 2 is equal to Number 1");

  // Do some comparisons with If statements using strings
  if (text1 == text2)
    console.log("Text 1 is equal to Text 2");
  else
    console.log("Text 1 is not equal to Text 2");

  if (text1 >= text2)
    console.log("Text 1 is greater than or equal to Text 2");
  else
    console.log("Text 1 is less than Text 2");

  // Switch statement
  switch (num2)
  {
    case 0:
      console.log("Number 2 is equal to 0");
      break;
    case 1:
      console.log("Number 2 is equal to 1");
      break;
    case 2:
      console.log("Number 2 is equal to 2");
      break;
    case 3:
      console.log("Number 2 is equal to 3");
      break;
    case 4:
      console.log("Number 2 is equal to 4");
      break;
    case 5:
      console.log("Number 2 is equal to 5");
      break;
    default:
      console.log("Number 2 is unknown value");
      break;
  }

  // Ternary operator
  num1 == num2
    ? console.log("Using Ternary Operator - Number 1 is equal to Number 2")
    : console.log("Using Ternary Operator - Number 1 is not equal to Number 2");
}

// =========================
// LOOP STATEMENTS
// =========================

function loops()
{
  // Create an array that we can loop over
  let shapes = new Array('Triangle', 'Circle', 'Square');
  let index = 0;  // ✅ ADD THIS

  // For Loop (prints all array elements)
  for (index = 0; index < shapes.length; ++index)
  {
    console.log("Using For Loop getting Array value of " + shapes[index] + " at " + index);
  }

  // For Loop (prints even indexes)
  for (index = 0; index < shapes.length; ++index)
  {
    if (index % 2 == 0)
    {
      console.log("Array value of " + shapes[index] + " at even index of " + index);
    }
  }

  // While Loop
  let i = 0;

  while (i < shapes.length)
  {
    console.log("Using While Loop getting Array value of " + shapes[i] + " at " + i);
    ++i;
  }

  // Do While Loop
  i = 0;

  do
  {
    console.log("Using Do While Loop getting Array value of " + shapes[i] + " at " + i);
    ++i;
  }
  while (i < shapes.length);
}

// =========================
// OBJECTS
// =========================

function objects()
{
  console.log("Inside objects()");

  // -----------------------------------
  // Object Literal (Person 1)
  // -----------------------------------
  let person1 =
  {
    firstName: "Bob",
    lastName: "Johnson",
    age: 25,
    occupation: "Student"
  };

  console.log(
    "This is Person 1 " +
    person1.firstName + " " +
    person1.lastName +
    " who is of age " +
    person1.age +
    " and is a " +
    person1.occupation
  );

  // -----------------------------------
  // Object using new Object() (Person 2)
  // -----------------------------------
  let person2 = new Object();

  person2.firstName = "Billy";
  person2.lastName = "White";
  person2.age = 35;
  person2.occupation = "Professor";

  console.log(
    "This is Person 2 " +
    person2.firstName + " " +
    person2.lastName +
    " who is of age " +
    person2.age +
    " and is a " +
    person2.occupation
  );

  // -----------------------------------
  // Constructor Function
  // -----------------------------------
  function Person(firstName, lastName, age, occupation)
  {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;              // ← FIXED (prof screenshot had typo)
    this.occupation = occupation;
  }

  let person3 = new Person("Mary", "Jackson", 50, "Dean");
  let person4 = new Person("John", "Lennon", 80, "Musician");

  console.log(
    "This is Person 3 " +
    person3.firstName + " " +
    person3.lastName +
    " who is of age " +
    person3.age +
    " and is a " +
    person3.occupation
  );

  console.log(
    "This is Person 4 " +
    person4.firstName + " " +
    person4.lastName +
    " who is of age " +
    person4.age +
    " and is a " +
    person4.occupation
  );

  // -----------------------------------
  // Enhanced Constructor + Method
  // -----------------------------------
  function EnhancedPerson(firstName, lastName, age, occupation)
  {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.occupation = occupation;

    this.display = function()
    {
      console.log(
        "This is an Enhanced Person " +
        this.firstName + " " +
        this.lastName +
        " who is of age " +
        this.age +
        " and is a " +
        this.occupation
      );
    };
  }

  let person5 = new EnhancedPerson("Paul", "McCartney", 78, "Musician");

  person5.display();
}

