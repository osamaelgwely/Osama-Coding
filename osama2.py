while True:

    Student_Name = input("Enter Student Name :")
    Student_Code = int(input("Enter Your Code :"))
    physics_degree = input("Enter the degree of physics :")
    Math_degree = input("Enter the degree of Math :")
    English_degree = input("Enter the degree of English :")
    Computer_degree = input("Enter the degree of Computer :")
    Max_degree = 400
    Final_Degree = float(physics_degree) + float(Math_degree) + float(English_degree) + float(Computer_degree)
    if Final_Degree > 400 :
        print(f"Error the Entered Total exceeds the allowed limit \nThe Correct Max degree is {Max_degree}")
        print("Please Re-Enter the degrees again")
        continue
    break 
            
Percentage = 100*(Final_Degree/Max_degree)
int_Percentage = int(Percentage)
print(f"The final degree is:{Final_Degree}")
print("Pertcentage of The Semester is",str(int_Percentage),"%")
if Final_Degree >= 90 and Percentage >= 90 :
    print("Exellent With A+")
    print("Congratulations")
elif Final_Degree >= 70 and Percentage >= 70 :
    print("Very Good with A")
elif Final_Degree >= 50 and Percentage >= 50 :
    print("Good")
else :
    print("Fail With F")   