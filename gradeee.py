import math

grade = float(input("Enter your grade? "))

Grade=math.ceil(grade)

if grade <= 65:
    print("You got Incomplete, Withdraw, Dropped.")
    print("Inc., W, D")
    print("Study Harder!")

elif grade >=65 and grade <= 75:
    print("Failure")
    print("You got 5.0")
    print("Study Hard!")

elif grade <= 75:
    print("You Got 3.0")
    print("Passing")
    print("Study Hard!")

elif grade >= 76 and grade <=78:
    print("You got 2.75")
    print("Satisfactory")

elif grade >=79 and grade <=81:
    print("You got 2.5")
    print("Satisfactory")

elif grade >= 82 and grade <=84:
    print("You got 2.25")
    print("Good")

elif grade >= 85 and grade <= 87:
    print("You got 2.0")
    print("Good")

elif grade >=88 and grade <= 90:
    print("You got 1.75")
    print("Very Good")

elif grade >= 91 and grade <=93:
    print("You got 1.5")
    print("Very Good")

elif grade >=94 and grade <= 96:
    print("You got 1.25")
    print("Excellent")

elif grade >= 97 and grade <= 100:
    print("You got 1.0")
    print("EXCELLENT!")

else:
    print("success") 