# Week 2: Making Decisions & Repeating Tasks in Python

## Project: Student Grade Calculator

This beginner project asks for a student's name and mark, checks that the mark is valid, assigns a letter grade, and prints an encouraging message.

## What you will learn

- `if`, `elif`, and `else` let a program choose an action.
- Comparison operators such as `>=` and `<=` compare values.
- A `while` loop repeats while input is invalid.
- Functions such as `grade_for()` and `message_for()` let us reuse named blocks of code.
- `try` and `except` handle text that cannot be changed into a whole number.

## Grading logic

| Marks | Grade |
| --- | --- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | F |

The program checks the highest threshold first. For example, a mark of 85 is not at least 90, but it is at least 80, so it receives a B.

## Files

- `grade_calculator.py` — interactive calculator.
- `test_cases.txt` — boundary and invalid-input examples to try manually.
- `screenshots/sample_run.png` — example run using Priya and 85 marks.

## Setup and run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Download or clone this project folder.
3. Open a terminal in the folder containing `grade_calculator.py`.
4. Run `python grade_calculator.py`. On some systems, use `python3 grade_calculator.py`.
5. Enter a student name and a whole-number mark from 0 to 100.

No third-party packages are needed.

## Example

```text
Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA:
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍
```

## Code structure

`grade_for(marks)` selects the grade with `if`/`elif`/`else`. `message_for(grade)` selects a friendly response from a dictionary. `get_valid_marks()` uses a `while` loop and `try`/`except` to repeat until the input is a whole number in range. `main()` connects these steps and prints the result.

## Testing evidence

Try all grade boundaries and invalid inputs listed in `test_cases.txt`. Confirm that marks below 0 or above 100 are rejected, non-numeric input prompts again, and valid marks produce the correct letter grade. The screenshot shows the sample case: Priya, 85, Grade B.

## Five-day practice plan

1. **Day 1 — Rules:** write the grading ranges on paper and notice where one range ends and the next begins.
2. **Day 2 — Input:** collect a name and mark, then print them.
3. **Day 3 — Decisions:** add the grade rules using `if`, `elif`, and `else`.
4. **Day 4 — Validation:** use a `while` loop and `try`/`except` so invalid marks are requested again.
5. **Day 5 — Functions:** run the cases in `test_cases.txt`, fix mistakes, and adjust the encouraging messages.

## What I learned

This project practices decision-making with grade thresholds, repetition with a validation loop, reusable functions, and basic error handling for invalid input.
