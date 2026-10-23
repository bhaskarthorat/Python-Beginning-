# # writr a program to check the username first and then check the password if the username is correct.
# username = (input("Enter username :"))
# if (username == "bhaskarthorat"):
#     print("username is correct")
#     password = input("Enter password : ")
#     if (password == "123"):
#         print("Login successful")
#     else:
#         print("wrong password ")    
# else:
#     print("Enter a valid username!")     

# write a progrsm to check whether a person is at least 18 years old and then check whether they are registered to vote

# age = int(input("Enter age to check eligibility to vote :"))
# if (age >= 18 and age <= 100):
#     print("Eligible for voting:")
#     registration = input("did the person register himself for voting? ")
#     if (registration == "yes"):
#         print("Registered")
#     else:
#         print("Not registered for voting!")
# else:
#     print("person is not eligible for voting!")        

#                 Match Case Practice questions


# 4 Quarters of a year


# quarter = input("Enter Month :")
# match quarter:
#     case "January"|"February"|"March":
#         print("1st Quarter of the year!")   
#     case "April"|"May"|"June":
#         print("2nd Quarter of the year!")
#     case "July"|"August"|"September":
#         print("3rd Quarter of the year!")
#     case "October"|"November"|"December":
#         print("4th Quarter of the year")    
#     case _:
#         print("Invalid Input!")             

# grade = input("Enter your grades : ")
# match grade:
#     case "A":
#         print("Marks between 90 to 100!")
#     case "B":
#         print("Marks between 80 to 89!")
#     case "C":
#         print("Marks between 70  to 79!")
#     case "D":
#         print("Marks between 60 to 69!")
#     case "E":
#         print("Marks between 50 to 59!")
#     case "F":
#         print("Marks between 0 to 49(Fail!!!)")    
#     case _:
#         print("Invalid Output!")                    



# """Using arithmatic operators for match case example!"""


# a = int(input("Enter Number : "))
# operator = input("Enter Operator (+,-,/,*)")
# b = int(input("Enter Number: "))

# # operator = input("Enter Operator (+,-,/,*)") 

# match operator:
#     case "+":
#         print("Addition",a+b)
#     case "-":
#         print("Subtraction",a-b)
#     case "/":
#         print("Division",a/b)   
#     case "*":
#         print("Multiplication",a*b)
#     case _:
#         print("invalid output")             