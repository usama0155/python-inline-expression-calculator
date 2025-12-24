# 🧮 Python Inline Expression Calculator

A simple yet smart Python CLI calculator that reads a **full math
expression in one line** (like `12+5`, `9 /3`, `7* 4`) --- removes
spaces, detects the operator, splits the operands, and evaluates the
result.

Built to practice:

-   🧠 Logic building
-   🔤 String parsing
-   ⚙️ Control flow & operators
-   🛡 Error handling (division-by-zero)

This project is small --- but it's intentional. I wrote the logic myself
instead of relying on built-in eval functions.

------------------------------------------------------------------------

## ✨ Features

-   ✔ Accepts full expressions in a single input
-   ✔ Supports `+`, `-`, `*`, `/`
-   ✔ Automatically removes spaces
-   ✔ Detects operator dynamically
-   ✔ Handles division-by-zero safely
-   ✔ Clean, readable, beginner-friendly code

------------------------------------------------------------------------

## 🧾 Example Usage

**Input**

    Enter Your Statements: 12 + 6

**Output**

    Output using + Operator: 18

------------------------------------------------------------------------

### More Examples

  Input     Output
  --------- -----------------------
  `7*3`     `21`
  `9 / 3`   `3.0`
  `15-4`    `11`
  `5/0`     `Cant Divide by zero`

------------------------------------------------------------------------

## 🧩 How It Works (Logic Breakdown)

1.  Takes full input as a single string
2.  Removes all spaces
3.  Loops through supported operators
4.  Splits the expression using the operator
5.  Converts operands to integers
6.  Passes values to calculation function

Keeps things:

-   modular
-   readable
-   easy to extend later

------------------------------------------------------------------------

## 🗂 Project Structure

    main()
     ├─ rec_conv_data()   → parses input & detects operator
     └─ calculations()    → performs operation & handles errors

------------------------------------------------------------------------

## 🚀 Future Improvements

Planned upgrades:

-   ⏳ Support decimal / floating-point numbers
-   🧪 Add invalid-input handling
-   ➕ Support exponent & modulus
-   🖥 GUI or web-based version
-   ⚡ Add automated tests

------------------------------------------------------------------------

## 🎯 Why I Built This

Instead of copying solutions, I wanted to:

-   break a problem into smaller steps
-   practice parsing logic
-   handle edge-cases manually
-   improve problem-solving skills

Sometimes "simple" projects teach the most.

------------------------------------------------------------------------

## 🤝 Feedback & Contributions

If you have ideas or improvements --- feel free to:

-   open an issue\
-   suggest enhancements\
-   fork and experiment

I'm always learning & iterating 🚀
