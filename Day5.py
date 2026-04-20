# Intro Message
print("Welcome to the Age and Student Checker!")

# Get the user's age and handle invalid inputs
try:
    age = int(input("How old are you?: "))
    if age < 0:
        print("Age can't be negative! Let's assume you are 0.")
        age = 0
except ValueError:
    print("That's not a valid number! Let's assume you are 20.")
    age = 20

# Get student status
student_answer = input("Are you a student? (yes/no) ").lower() # Convert to lower case for consistency

# Check if the answer is valid and set a variable
is_student = False # Default to False
if student_answer == "yes":
    is_student = True
elif student_answer == "no":
    is_student = False
else:
    print("I'll take that as a 'no' since you didn't say 'yes' or 'no' clearly.")

# Custom messages based on age and student status
if age >= 13 and age <=19 and is_student:
    print("You're a teenage student-probably juggling homework and TikTok!")
elif age >= 20 and is_student:
    print("You're a student over 20-hope you're enjoying college life!")
elif age >=13 and age <=19 and not is_student:
    print("Your'e a teen but not a student? Living the free life!")
else:
    print(f"At {age}, you're navigating life-student or not, keep rocking it!")

print("Thanks for playing!")
