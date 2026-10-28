"""A friendly first Python program that introduces a learner to programming."""

print("Welcome to your personal introduction program!")
print("Let's get to know you.\n")

name = input("What is your name? ").strip()
age_text = input("How old are you? ").strip()
hobby = input("What is your favorite hobby? ").strip()

# Keep the original answer as text so the program stays welcoming for all ages.
print(f"\n🎉 Welcome, {name}! 🎉")
print(f"You are {age_text} years old and love {hobby}.")
print("Thanks for sharing a little about yourself!")
