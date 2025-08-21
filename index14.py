percentage = float(input("Enter your percentage: "))

if percentage < 25:
    print("Grade: D")
elif percentage >= 25 and percentage < 45:
    print("Grade: C")
elif percentage >= 45 and percentage < 65:
    print("Grade: B")
elif percentage >= 65 and percentage < 85:
    print("Grade: A")
elif percentage >= 85:
    print("Grade: A+")
else:
    print("Invalid input")
