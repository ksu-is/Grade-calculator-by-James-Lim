#This will serve as my code in the visual studio code
import statistics #Built in function to calculate mathematical statistics of numeric data.
grades = []
while():
    classes = input("What class are you trying to calculate your grade in? ")


while len(grades) < 5: # counts up the total attempts grades has untill its over 5
    user_input = input(f"Enter the score for assignment {len(grades) + 1}: ") # F string used to help append items until into the list
    user_input = int(user_input)
    if 0 <= user_input <= 100:  # Make sure the score is between 0 and 100
        grades.append(user_input)
    else:
        print("Please enter a number between the ranges of 0-100")
print(grades)
grades_score = statistics.mean(grades)
print(grades_score)
def system(grades_score): # This is where the grade is scored on a letter basis
    if grades_score >= 90:
        print("Your score for the class is currently an A") 
        return "A"
    elif grades_score >= 80:
        print("Your score for the class is currently a B")
    elif grades_score >= 70:
        print("Your score for the class is curently a C")
    elif grades_score >= 60:
        print("Your score for the class is currently a D")
    else:
        print("Your score for the class is currently a F")
final_grade = system(grades_score)
print("Your total score in" , classes , "is currently " , final_grade)