
from flask import Flask, render_template_string

app = Flask(__name__)

page = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>My Calculator</title>

<style>
* {
    box-sizing: border-box;
}

body {
    background: #10101c;
    color: white;
    font-family: Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
}

.calculator {
    background: #1c1c2e;
    padding: 25px;
    border-radius: 25px;
    width: 340px;
    box-shadow: 0 10px 35px #000;
}

h2 {
    color: #a78bfa;
    text-align: center;
}

#display {
    width: 100%;
    height: 85px;
    background: #10101c;
    border: none;
    border-radius: 15px;
    color: white;
    font-size: 32px;
    text-align: right;
    padding: 15px;
    margin-bottom: 20px;
}

.buttons {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

button {
    height: 65px;
    border: none;
    border-radius: 15px;
    background: #303047;
    color: white;
    font-size: 22px;
    cursor: pointer;
}

button:active {
    transform: scale(0.94);
}

.operator {
    background: #7048e8;
}

.clear {
    background: #e34b65;
}

.equal {
    background: #16a085;
    grid-column: span 2;
}
</style>
</head>

<body>

<div class="calculator">

<h2>MY CALCULATOR</h2>

<input id="display" value="0" readonly>

<div class="buttons">

<button class="clear" onclick="clearDisplay()">C</button>
<button onclick="removeLast()">⌫</button>
<button class="operator" onclick="add('/')">÷</button>
<button class="operator" onclick="add('*')">×</button>

<button onclick="add('7')">7</button>
<button onclick="add('8')">8</button>
<button onclick="add('9')">9</button>
<button class="operator" onclick="add('-')">−</button>

<button onclick="add('4')">4</button>
<button onclick="add('5')">5</button>
<button onclick="add('6')">6</button>
<button class="operator" onclick="add('+')">+</button>

<button onclick="add('1')">1</button>
<button onclick="add('2')">2</button>
<button onclick="add('3')">3</button>
<button onclick="add('.')">.</button>

<button onclick="add('0')">0</button>
<button class="equal" onclick="calculate()">=</button>

</div>
</div>

<script>
let display = document.getElementById("display");
let expression = "";

function add(value) {
    if (expression === "Error") expression = "";

    if (expression === "" && "+*/".includes(value)) {
        return;
    }

    expression += value;
    display.value = expression;
}

function clearDisplay() {
    expression = "";
    display.value = "0";
}

function removeLast() {
    expression = expression.slice(0, -1);
    display.value = expression || "0";
}

function calculate() {
    try {
        if (!/^[0-9+*/. -]+$/.test(expression)) {
            throw new Error();
        }

        let result = Function(
            '"use strict"; return (' + expression + ')'
        )();

        if (!Number.isFinite(result)) {
            throw new Error();
        }

        expression = String(
            Number(result.toPrecision(10))
        );

        display.value = expression;

    } catch {
        expression = "Error";
        display.value = "Error";
    }
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
  
