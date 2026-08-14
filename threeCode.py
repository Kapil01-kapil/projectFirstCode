from colorama import Fore, Style, init

init(autoreset=True)

# Anubhav Trainings Course Selection Program - Dictionary Version
course_catalog = {
    "UI5": {"trainer": "Anubhav", "hours": 40, "price": 380},
    "CPI": {"trainer": "Anurag", "hours": 35, "price": 400},
    "AOH": {"trainer": "Anubhav", "hours": 40, "price": 400},
    "CDS": {"trainer": "Ananya", "hours": 50, "price": 480},
    "BTP": {"trainer": "Saurabh", "hours": 30, "price": 500},
    "SAC": {"trainer": "Rohan", "hours": 45, "price": 300},
    "CAPM": {"trainer": "Sonia", "hours": 60, "price": 900},
    "RAP": {"trainer": "Anubhav", "hours": 40, "price": 850}
}

# Store selected courses
selected_courses = []

# Welcome message
print(Fore.GREEN + Style.BRIGHT + "Welcome to", end=" ")
print(Fore.MAGENTA + Style.BRIGHT + "Anubhav Trainings", end=" ")
print(Fore.CYAN + Style.BRIGHT + "Following Excellence", end=" ")
print(Fore.YELLOW + Style.BRIGHT + "with", end=" ")
print(Fore.WHITE + Style.BRIGHT + "Sheer Passion!")

# Ask for courses
while True:
    course = input(
        "\nEnter the course name (or type 'exit' to finish): "
    ).strip().upper()

    if course == "EXIT":
        break

    elif course in course_catalog:
        selected_courses.append(course)
        print(f"Added {course} to your selection.")

    else:
        print(f"Course {course} not found. Please try again.")

# Display selected courses
print("\nYou have selected the following courses:")

total_amount = 0

for idx, course in enumerate(selected_courses, start=1):
    details = course_catalog[course]

    print(
        f"{idx}. {course} - "
        f"Trainer: {details['trainer']}, "
        f"Hours: {details['hours']}, "
        f"Price: ${details['price']}"
    )

    total_amount += details["price"]

print(f"\nTotal amount for selected courses: ${total_amount}")