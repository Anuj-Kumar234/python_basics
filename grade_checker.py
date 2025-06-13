marks =int(input("Enter the marks: "))
if 0 > marks or marks>100:
    print("Invalid Entry")
elif 90 <= marks <= 100:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
elif marks>=40:
    print("Grade D")
elif marks>=33:
    print("Just pass !")
elif(marks<33):
    print("Grade E , FAIL !")
else:
    print("Please enter marks between 0-100")


     
