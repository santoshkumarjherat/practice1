#Greeting and Calculate student Grade
name = input("Enter your name: ")

#Greet With Name
print("\nAs-Salaam-Alaikum," " " + name)
print("Hope you Doing Damn Good")

#Adding subjects marks
print("\nEnter your English Subject Marks:")
eng_marks = int(input())
if eng_marks > 100:
    print("Invalid Input.. Please Try Again")

print("Enter your Mathematics Subject Marks:")
math_marks = int(input())

print("Enter your Chemistry Subject Marks:")
chem_marks = int(input())

print("Enter your Physics Subject Marks:")
phy_marks = int(input())

print("Enter your Computer Subject Marks:")
com_marks = int(input())

#Sum of all the subject marks:
total_obtained_marks = eng_marks + math_marks + chem_marks + phy_marks + com_marks
print("Your Obtained marks:",total_obtained_marks)

#total marks of subject
total_marks = 500

#calculate %age
percentage = total_obtained_marks/total_marks * 100

#calculating grade
if  percentage >= 81 and percentage <= 100:
    print("You are a Position Holder!")
    print(f"Your percentage is:{percentage}%")
    
elif percentage >= 71 and  percentage < 81:
    print("Your Grade is 'A'")
    print(f"Your percentage is:{percentage}%")

elif percentage >= 61 and  percentage < 71:
    print("Your Grade is 'B'")
    print(f"Your percentage is:{percentage}%")

elif percentage >= 51 and  percentage < 61:
    print("Your Grade is 'C'")
    print(f"Your percentage is:{percentage}%")

elif percentage >= 41 and  percentage < 51:
    print("Your Grade is 'D'")
    print(f"Your percentage is:{percentage}%")
    
elif percentage >= 31 and  percentage < 41:
    print("Your Grade is 'E'")
    print(f"Your percentage is:{percentage}%")
    
elif percentage >= 0 and  percentage < 31:
    print("You are Failed... Hard work Next Time")
    print(f"Your percentage is:{percentage}%")
    
else:
    print("Invailed input...Pleasse try again")
