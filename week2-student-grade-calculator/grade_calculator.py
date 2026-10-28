"""Ask for a student's name and marks, then display a friendly grade."""

# Example run:
# Enter student name: Priya
# Enter marks (0-100): 85
#
# 📊 RESULT FOR PRIYA:
# Marks: 85/100
# Grade: B
# Message: Very Good! Keep it up! 👍


def grade_for(marks):
    """Return the letter grade for a mark from 0 through 100."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def message_for(grade):
    """Return an encouraging message for a letter grade."""
    messages = {
        "A": "Excellent work! Keep shining! 🌟",
        "B": "Very Good! Keep it up! 👍",
        "C": "Good effort! Keep practicing and you will improve! 💪",
        "D": "You passed. Review a little more and keep going! 📘",
        "F": "Don't give up. Every attempt helps you learn! 🌱",
    }
    return messages[grade]


def get_valid_marks():
    """Ask again until the user enters a whole-number mark from 0 to 100."""
    while True:
        answer = input("Enter marks (0-100): ").strip()

        try:
            marks = int(answer)
        except ValueError:
            print("Please enter a whole number, such as 85.")
            continue

        if 0 <= marks <= 100:
            return marks

        print("Marks must be between 0 and 100. Please try again.")


def main():
    """Run the student grade calculator."""
    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade = grade_for(marks)

    print(f"\n📊 RESULT FOR {name.upper()}: ")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message_for(grade)}")


if __name__ == "__main__":
    main()
