"use strict";


/* =========================================================
   PAGE ELEMENTS
   ========================================================= */

const calculatorDisplay =
    document.getElementById("calculatorDisplay");

const calculatorHistory =
    document.getElementById("calculatorHistory");

const calculatorButtons =
    document.getElementById("calculatorButtons");

const darkModeToggle =
    document.getElementById("darkModeToggle");

const currentYear =
    document.getElementById("currentYear");


/* =========================================================
   CALCULATOR STATE
   ========================================================= */

let calculatorExpression = "";
let calculatorJustFinished = false;

const maximumExpressionLength = 28;


/* =========================================================
   DISPLAY HELPERS
   ========================================================= */

function convertExpressionForDisplay(expression) {

    return expression
        .replaceAll("*", "\u00D7")
        .replaceAll("/", "\u00F7")
        .replaceAll("-", "\u2212");

}


function updateCalculatorDisplay() {

    if (!calculatorDisplay) {
        return;
    }

    calculatorDisplay.value =
        calculatorExpression
            ? convertExpressionForDisplay(
                calculatorExpression
            )
            : "0";

}


function showCalculatorError(message) {

    if (calculatorHistory) {

        calculatorHistory.textContent =
            message;

    }

    calculatorExpression = "Error";
    calculatorJustFinished = true;

    updateCalculatorDisplay();

}


function resetAfterError() {

    if (calculatorExpression === "Error") {

        calculatorExpression = "";
        calculatorJustFinished = false;

    }

}


/* =========================================================
   VALUE ENTRY
   ========================================================= */

function isOperator(value) {

    return [
        "+",
        "-",
        "*",
        "/"
    ].includes(value);

}


function getCurrentNumberSegment() {

    const parts =
        calculatorExpression.split(
            /[+\-*/]/
        );

    return parts[parts.length - 1];

}


function appendNumberOrDecimal(value) {

    resetAfterError();

    if (calculatorJustFinished) {

        calculatorExpression = "";
        calculatorJustFinished = false;

        if (calculatorHistory) {

            calculatorHistory.innerHTML =
                "&nbsp;";

        }

    }


    if (
        calculatorExpression.length >=
        maximumExpressionLength
    ) {

        return;

    }


    if (value === ".") {

        const currentNumber =
            getCurrentNumberSegment();

        if (currentNumber.includes(".")) {

            return;

        }

        if (
            calculatorExpression === "" ||
            isOperator(
                calculatorExpression.slice(-1)
            )
        ) {

            calculatorExpression += "0.";

        } else {

            calculatorExpression += ".";

        }

    } else {

        const currentNumber =
            getCurrentNumberSegment();

        if (currentNumber === "0") {

            calculatorExpression =
                calculatorExpression.slice(
                    0,
                    -1
                ) + value;

        } else {

            calculatorExpression += value;

        }

    }

    updateCalculatorDisplay();

}


function appendOperator(operator) {

    resetAfterError();

    calculatorJustFinished = false;


    if (calculatorExpression === "") {

        if (operator === "-") {

            calculatorExpression = "-";
            updateCalculatorDisplay();

        }

        return;

    }


    const finalCharacter =
        calculatorExpression.slice(-1);


    if (isOperator(finalCharacter)) {

        if (
            calculatorExpression === "-" &&
            operator !== "-"
        ) {

            return;

        }

        calculatorExpression =
            calculatorExpression.slice(
                0,
                -1
            ) + operator;

    } else if (finalCharacter === ".") {

        calculatorExpression +=
            "0" + operator;

    } else {

        calculatorExpression += operator;

    }

    updateCalculatorDisplay();

}


/* =========================================================
   CLEAR AND BACKSPACE
   ========================================================= */

function clearCalculator() {

    calculatorExpression = "";
    calculatorJustFinished = false;

    if (calculatorHistory) {

        calculatorHistory.innerHTML =
            "&nbsp;";

    }

    updateCalculatorDisplay();

}


function removeLastCharacter() {

    resetAfterError();

    calculatorJustFinished = false;

    calculatorExpression =
        calculatorExpression.slice(
            0,
            -1
        );

    updateCalculatorDisplay();

}


/* =========================================================
   EXPRESSION PARSER
   ========================================================= */

function tokenizeExpression(expression) {

    const tokens = [];

    let numberBuffer = "";


    for (
        let index = 0;
        index < expression.length;
        index += 1
    ) {

        const character =
            expression[index];


        if (
            (
                character >= "0" &&
                character <= "9"
            ) ||
            character === "."
        ) {

            numberBuffer += character;
            continue;

        }


        if (isOperator(character)) {

            const previousCharacter =
                expression[index - 1];


            const isUnaryNegative =
                character === "-" &&
                (
                    index === 0 ||
                    isOperator(previousCharacter)
                );


            if (isUnaryNegative) {

                numberBuffer = "-";
                continue;

            }


            if (
                numberBuffer === "" ||
                numberBuffer === "-"
            ) {

                throw new Error(
                    "Incomplete expression."
                );

            }


            const numberValue =
                Number(numberBuffer);


            if (!Number.isFinite(numberValue)) {

                throw new Error(
                    "Invalid number."
                );

            }


            tokens.push(numberValue);
            tokens.push(character);

            numberBuffer = "";

        } else {

            throw new Error(
                "Unsupported character."
            );

        }

    }


    if (
        numberBuffer === "" ||
        numberBuffer === "-"
    ) {

        throw new Error(
            "Incomplete expression."
        );

    }


    const finalNumber =
        Number(numberBuffer);


    if (!Number.isFinite(finalNumber)) {

        throw new Error(
            "Invalid number."
        );

    }


    tokens.push(finalNumber);

    return tokens;

}


/* =========================================================
   SAFE CALCULATION

   Multiplication and division are completed first.
   Addition and subtraction are completed second.
   ========================================================= */

function evaluateTokens(tokens) {

    const firstPass = [
        tokens[0]
    ];


    for (
        let index = 1;
        index < tokens.length;
        index += 2
    ) {

        const operator =
            tokens[index];

        const nextNumber =
            tokens[index + 1];


        if (
            operator === "*" ||
            operator === "/"
        ) {

            const currentNumber =
                firstPass.pop();


            if (
                operator === "/" &&
                nextNumber === 0
            ) {

                throw new Error(
                    "Cannot divide by zero."
                );

            }


            const combinedValue =
                operator === "*"
                    ? currentNumber * nextNumber
                    : currentNumber / nextNumber;


            firstPass.push(
                combinedValue
            );

        } else {

            firstPass.push(operator);
            firstPass.push(nextNumber);

        }

    }


    let result =
        firstPass[0];


    for (
        let index = 1;
        index < firstPass.length;
        index += 2
    ) {

        const operator =
            firstPass[index];

        const nextNumber =
            firstPass[index + 1];


        if (operator === "+") {

            result += nextNumber;

        } else if (operator === "-") {

            result -= nextNumber;

        }

    }


    if (!Number.isFinite(result)) {

        throw new Error(
            "Result is outside the supported range."
        );

    }


    return result;

}


function formatCalculatorResult(result) {

    const roundedResult =
        Number(
            result.toFixed(10)
        );


    if (
        Math.abs(roundedResult) >= 1e15 ||
        (
            Math.abs(roundedResult) > 0 &&
            Math.abs(roundedResult) < 1e-9
        )
    ) {

        return roundedResult.toExponential(8);

    }


    return String(roundedResult);

}


/* =========================================================
   CALCULATE RESULT
   ========================================================= */

function calculateResult() {

    resetAfterError();


    if (!calculatorExpression) {

        return;

    }


    const finalCharacter =
        calculatorExpression.slice(-1);


    if (
        isOperator(finalCharacter) ||
        finalCharacter === "."
    ) {

        showCalculatorError(
            "Complete the expression before calculating."
        );

        return;

    }


    try {

        const originalExpression =
            calculatorExpression;

        const tokens =
            tokenizeExpression(
                calculatorExpression
            );

        const result =
            evaluateTokens(tokens);

        const formattedResult =
            formatCalculatorResult(result);


        if (calculatorHistory) {

            calculatorHistory.textContent =
                convertExpressionForDisplay(
                    originalExpression
                ) + " =";

        }


        calculatorExpression =
            formattedResult;

        calculatorJustFinished =
            true;

        updateCalculatorDisplay();

    } catch (error) {

        showCalculatorError(
            error.message ||
            "Unable to calculate the expression."
        );

    }

}


/* =========================================================
   BUTTON EVENTS
   ========================================================= */

if (calculatorButtons) {

    calculatorButtons.addEventListener(
        "click",
        function (event) {

            const selectedButton =
                event.target.closest(
                    "button"
                );


            if (!selectedButton) {

                return;

            }


            const buttonValue =
                selectedButton.dataset.value;

            const buttonAction =
                selectedButton.dataset.action;


            if (buttonValue) {

                if (isOperator(buttonValue)) {

                    appendOperator(
                        buttonValue
                    );

                } else {

                    appendNumberOrDecimal(
                        buttonValue
                    );

                }

                return;

            }


            switch (buttonAction) {

                case "clear":

                    clearCalculator();
                    break;


                case "backspace":

                    removeLastCharacter();
                    break;


                case "calculate":

                    calculateResult();
                    break;


                default:

                    break;

            }

        }
    );

}


/* =========================================================
   KEYBOARD SUPPORT
   ========================================================= */

document.addEventListener(
    "keydown",
    function (event) {

        const activeElement =
            document.activeElement;

        const userIsTypingElsewhere =
            activeElement &&
            (
                activeElement.tagName === "INPUT" ||
                activeElement.tagName === "TEXTAREA" ||
                activeElement.tagName === "SELECT"
            ) &&
            activeElement !== calculatorDisplay;


        if (userIsTypingElsewhere) {

            return;

        }


        const key =
            event.key;


        if (
            key >= "0" &&
            key <= "9"
        ) {

            event.preventDefault();

            appendNumberOrDecimal(
                key
            );

            return;

        }


        if (key === ".") {

            event.preventDefault();

            appendNumberOrDecimal(
                "."
            );

            return;

        }


        if (
            key === "+" ||
            key === "-" ||
            key === "*" ||
            key === "/"
        ) {

            event.preventDefault();

            appendOperator(
                key
            );

            return;

        }


        if (
            key === "Enter" ||
            key === "="
        ) {

            event.preventDefault();

            calculateResult();

            return;

        }


        if (key === "Backspace") {

            event.preventDefault();

            removeLastCharacter();

            return;

        }


        if (
            key === "Escape" ||
            key === "Delete"
        ) {

            event.preventDefault();

            clearCalculator();

        }

    }
);


/* =========================================================
   CURRENT COPYRIGHT YEAR
   ========================================================= */

if (currentYear) {

    currentYear.textContent =
        new Date().getFullYear();

}


/* =========================================================
   WEBSITE THEME

   Light Mode is the default.
   ========================================================= */

const themeStorageKey =
    "ghostlineTheme";


function applyGhostlineTheme(theme) {

    const useDarkMode =
        theme === "dark";


    document.body.classList.toggle(
        "dark-mode",
        useDarkMode
    );


    document.body.classList.toggle(
        "light-mode",
        !useDarkMode
    );


    if (darkModeToggle) {

        darkModeToggle.textContent =
            useDarkMode
                ? "Light Mode"
                : "Dark Mode";


        darkModeToggle.setAttribute(
            "aria-pressed",
            String(useDarkMode)
        );

    }

}


/*
   Remove the legacy theme key used by the
   original calculator page.
*/

localStorage.removeItem("theme");


const savedTheme =
    localStorage.getItem(
        themeStorageKey
    );


const startingTheme =
    savedTheme === "dark"
        ? "dark"
        : "light";


applyGhostlineTheme(
    startingTheme
);


if (darkModeToggle) {

    darkModeToggle.addEventListener(
        "click",
        function () {

            const darkModeIsActive =
                document.body.classList.contains(
                    "dark-mode"
                );


            const newTheme =
                darkModeIsActive
                    ? "light"
                    : "dark";


            localStorage.setItem(
                themeStorageKey,
                newTheme
            );


            applyGhostlineTheme(
                newTheme
            );

        }
    );

}


/* =========================================================
   CLOSE MOBILE NAVIGATION
   ========================================================= */

document.querySelectorAll(
    ".navbar-nav .nav-link"
).forEach(function (navigationLink) {

    navigationLink.addEventListener(
        "click",
        function () {

            const navigationMenu =
                document.getElementById(
                    "mainNavigation"
                );


            if (
                navigationMenu &&
                navigationMenu.classList.contains(
                    "show"
                )
            ) {

                $(".navbar-collapse").collapse(
                    "hide"
                );

            }

        }
    );

});


/* =========================================================
   INITIAL DISPLAY
   ========================================================= */

updateCalculatorDisplay();