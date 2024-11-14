#This will serve as my code in the visual studio code
import statistics
grades = []
classes = input("What class are you trying to calculate your grade in? ")

while len(grades) < 5: # counts up the total attempts grades has untill its over 5
    user_input = input(f"Enter the score for the last 5 assignment.  ")
    user_input = len(grades) + 1
    user_input = int(user_input)
    if 0 <= user_input <= 100:  # Make sure the score is between 0 and 100
        grades.append(user_input)
    else:
        print("Please enter a number between the ranges of 0-100")

grades_score = statistics.mean(grades)
print(grades_score)
def system(grades_score): 
    if grades_score >= 90:
        print("Your score for the class is currently a A") 
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