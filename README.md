# Week 1: Python Basics — Your First Steps in Programming

A beginner-friendly project that practices `input()`, variables, strings, and `print()` by asking three questions and displaying a personal welcome.

## What you will learn

- A program is a sequence of instructions a computer follows.
- Variables give names to stored values, such as `name`, `age_text`, and `hobby`.
- `input()` reads text typed by the user. `print()` displays text.
- Strings hold text. An f-string inserts variable values into a message, for example `f"Welcome, {name}!"`.
- `+`, `-`, `*`, and `/` perform addition, subtraction, multiplication, and division. Try `print(8 + 2)` in the Python prompt.
- Lists collect several values: `foods = ["mango", "rice", "pasta"]`; use `foods[0]` to get the first item (Python counts from zero).

## Requirements

Python 3. No extra packages are needed; see `requirements.txt`.

## Setup and run

1. Install Python 3 from [python.org](https://www.python.org/downloads/) (on Windows, enable **Add Python to PATH** in the installer). On macOS or Linux, use the official installer or your operating system's package manager.
2. Download and unzip this project, then open a terminal in the unzipped `week1-python-basics` folder.
3. Run `python personal_intro.py`. If your system uses a separate Python 3 command, run `python3 personal_intro.py` instead.
4. Answer the name, age, and hobby questions and read your welcome message.

You can also paste the code into [Google Colab](https://colab.research.google.com/) and run the cell if you cannot install Python yet.

## Project files

- `personal_intro.py` — the runnable program.
- `README.md` — this guide and learning notes.
- `requirements.txt` — confirms there are no third-party dependencies.
- `screenshot.png` — sample terminal output (illustration).

## Code structure and technical details

The program runs top to bottom. It prints an introduction, asks three questions, stores each answer in a variable, then uses two f-strings to personalize the result. The inputs are kept as strings; this is enough to display the age and avoids converting text into a number before we have learned input validation. The program uses no lists or external libraries; try the list example under “What you will learn” separately.

## Example run

```text
Welcome to your personal introduction program!
Let's get to know you.

What is your name? Alex
How old are you? 21
What is your favorite hobby? Coding

🎉 Welcome, Alex! 🎉
You are 21 years old and love Coding.
Thanks for sharing a little about yourself!
```

## Testing evidence

Manual example: enter `Alex`, `21`, and `Coding`. The program should ask all three questions in order and include all three answers in its final message. Try another name, age, and hobby to see the output change. Empty answers are accepted in this first version; input validation is a useful next exercise.

## Five-day practice plan

1. **Day 1 — Setup:** install Python, run this file, and try `print("Hello, World!")`.
2. **Day 2 — Input:** identify each `input()` call and the variable that stores its answer.
3. **Day 3 — Welcome:** change the f-string wording and run the program again.
4. **Day 4 — Enhance:** add a question about the user's favorite food and display the answer.
5. **Day 5 — Review:** test several answers, add a comment, and check spelling and formatting.

## What I learned

This project demonstrates how a Python program runs one instruction at a time, how variables store user answers, and how `input()`, `print()`, strings, and f-strings work together. It also introduces basic arithmetic and list indexing as short practice examples.
