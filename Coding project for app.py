import statistics  # Built-in function to calculate mathematical statistics of numeric data, helpful in finding the average 1
grades_dict = {}  # Empty dictionary created over here to store the grades for mutiple assignments and is useful as a quality of life update. 6 
subjects = []
num_classes = int(input("How many classes are you trying to calculate your grade in? "))

for i in range(num_classes):  # This is used to loop over the number of classes to input subject names as well as more effecient rather than hard coding it. 5
    subject = input(f"Enter the name of class {i+1}: ")
    subjects.append(subject)

for subject in subjects: 
    grades = []  # Store grades for the current subject
    print(f"\nEntering grades for {subject}:")

    while len(grades) < 5:  # counts up the total attempts grades has untill its over 5. Useful counter for the number of assignments. 2
        user_input = int(input(f"Enter the score for assignment {len(grades) + 1}: "))  # F string used to help append items until into the list which is useful for the counting system. 4
        if 0 <= user_input <= 100:  # Ensure the score is between 0 and 100 
            grades.append(user_input)
        else:
            print("Please enter a number between the ranges of 0-100")
    
    # Calculate average score for the current subject
    grades_score = statistics.mean(grades)
    print(f"Average score for {subject}: {grades_score}")

    # Store grades in the dictionary
    grades_dict[subject] = grades_score

    # Calculate letter grade
    def system(grades_score):  # This is where the grade is scored on a letter basis, this helpful in displaying different facet of information. 3
        if grades_score >= 90:
            print("Your score for the class is currently an A")
            return "A"
        elif grades_score >= 80:
            print("Your score for the class is currently a B")
            return "B"
        elif grades_score >= 70:
            print("Your score for the class is currently a C")
            return "C"
        elif grades_score >= 60:
            print("Your score for the class is currently a D")
            return "D"
        else:
            print("Your score for the class is currently a F")
            return "F"

    final_grade = system(grades_score)

# Optionally, display all final grades for all subjects at the end
print("\nSummary of all subjects and grades:")
for subject, avg_score in grades_dict.items():
    final_grade = system(avg_score)
    print(f"{subject}: Average Score: {avg_score}, Final Grade: {final_grade}")

