# 1 creating a program that displays "Good Morning" to 7 employees, one time for each employee.

for i in range(1,8):
    print("Good Morning Employee",(i))


# 2 A teacher wants to print roll numbers from 1 to 30.
for i in range(1,31):
    print("Roll no 1",(i))


# 3 A timer must display numbers from 10 down to 1 before starting.    

for i in range(10,0,-1):
    print(i)

# 4 A shopkeeper wants to display even numbers from 2 to 20 for a billing demonstration

for i in range(2,21,2):
    print(i)

# 5 A teacher needs all odd numbers from 1 to 25.

for i in range(1,26,2):
    print(i)

# 6 A school needs to print "Present" for each of 40 students while taking attendance.
for i in range(1,41):
    print("Student no ",(i),"Present!")   

# 7 A bus has 45 seats. Display seat numbers from 1 to 45.
for i in range(1,46):
    print("Seat no -->",(i))     

# 8 A device displays temperatures of 0, 5, 10, 15, and so on, up to 50
for i in range(0,51,5):
    print("Temperature -->",(i))

# 9  An elevator display shows floors from 0 through 12 as it moves upward.

for i in range(12,-1,-1):
    print("Floor no :",(i)) 

# 10 A theatre wants to display seat numbers from 20 down to 1.
for i in range(20,0,-1):
    print("Seat no :",(i))

# 11 A person saves ₹100 every day for 30 days. Calculate the total savings.

total = 0
for i in range(1,31):
    total = total + 100
print("Total Savings :",total)


# 12 A customer buys 5 items with prices ₹50, ₹100, ₹150, ₹200 and ₹250. Calculate the total bill.

total = 0
for i in range(1,6):
    price = int(input("Enter price of item :"))
    total = total + price
print("Total Bill :",total)


# 13 A student wants to display the multiplication table of a number entered by the user.

num = int(input("Enter a number :"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


# 14 A student has marks of 65, 78, 82, 90 and 75 in five subjects. Calculate the total marks.

total = 0
for i in range(1,6):
    marks = int(input("Enter marks :"))
    total = total + marks
print("Total Marks :",total)


# 15 A program must count how many even numbers exist between 1 and 100.

count = 0
for i in range(1,101):
    if i % 2 == 0:
        count = count + 1
print("Total Even Numbers :",count)


# 16 An electricity meter records daily usage for 7 days. Calculate the total consumption.

total = 0
for i in range(1,8):
    units = int(input("Enter units consumed :"))
    total = total + units
print("Total Consumption :",total)


# 17 A mathematics teacher wants the product of all integers from 1 to 5.

product = 1
for i in range(1,6):
    product = product * i
print("Product :",product)


# 18 A shop prints all numbers from 1 to 100 that are divisible by 5.

for i in range(1,101):
    if i % 5 == 0:
        print(i)


# 19 A teacher wants to display every number from 1 to 15 alongside its square.

for i in range(1,16):
    print("Number :",i,"Square :",i**2)


# 20 A student has marks in 4 subjects. Calculate the average marks.

total = 0
for i in range(1,5):
    marks = int(input("Enter marks :"))
    total = total + marks
print("Average Marks :",total/4)


# 21 An ATM records 5 withdrawal attempts. Count how many attempts failed.

count = 0
for i in range(1,6):
    status = input("Enter status (success/failed) :")
    if status == "failed":
        count = count + 1
print("Failed Attempts :",count)


# 22 A teacher has marks for 6 students. Count how many students passed with 35 or more marks.

count = 0
for i in range(1,7):
    marks = int(input("Enter marks :"))
    if marks >= 35:
        count = count + 1
print("Students Passed :",count)


# 23 A shop has stock quantities for 6 products. Count how many products are out of stock.

count = 0
for i in range(1,7):
    stock = int(input("Enter stock quantity :"))
    if stock == 0:
        count = count + 1
print("Out of Stock Products :",count)


# 24 A login system records 5 attempts. Count how many times the wrong password was entered.

count = 0
for i in range(1,6):
    status = input("Enter attempt status (correct/wrong) :")
    if status == "wrong":
        count = count + 1
print("Wrong Attempts :",count)


# 25 A store gives a discount to customers whose purchase amount is at least ₹1000. Count eligible customers.

count = 0
for i in range(1,6):
    amount = int(input("Enter purchase amount :"))
    if amount >= 1000:
        count = count + 1
print("Eligible Customers :",count)


# 26 A weather station records temperatures. Display only temperatures above 30 degrees.

for i in range(1,6):
    temperature = int(input("Enter temperature :"))
    if temperature > 30:
        print("Temperature :",temperature)


# 27 An office stores salaries of 4 employees. Display the revised salary after a 10% increment.

for i in range(1,5):
    salary = int(input("Enter salary :"))
    increment = salary * 10 / 100
    revised_salary = salary + increment
    print("Revised Salary :",revised_salary)


# 28 A teacher wants multiplication tables for 2, 3 and 4, from 1 to 10.

for i in range(2,5):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()


# 29 A classroom has 4 rows and 5 seats in every row. Display every row and seat combination.

for i in range(1,5):
    for j in range(1,6):
        print("Row",i,"Seat",j)


# 30 A program should display five lines of stars, starting with one star and adding one star on every new line.

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


# 31 You deposit ₹10000 into a bank account earning 5% annual interest. Calculate the balance after each of 5 years.

balance = 10000
for i in range(1,6):
    interest = balance * 5 / 100
    balance = balance + interest
    print("Year",i,"Balance :",balance)


# 32 A game stores 6 guesses. Count how many guesses are greater than 20.

count = 0
for i in range(1,7):
    guess = int(input("Enter guess :"))
    if guess > 20:
        count = count + 1
print("Guesses Greater Than 20 :",count)


# 33 A school wants all numbers from 1 to 100 divisible by both 3 and 5.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 34 A user enters a positive integer. Display all its positive factors.

num = int(input("Enter a number :"))
for i in range(1,num+1):
    if num % i == 0:
        print(i)


# 35 A user enters a number. Check whether it is a prime number.

num = int(input("Enter a number :"))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# 36 A user enters a number such as 121 or 1331. Check whether it is a palindrome.

num = int(input("Enter a number :"))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 37 A program must display the first 10 numbers of the Fibonacci sequence, beginning with 0 and 1.

a = 0
b = 1
for i in range(1,11):
    print(a)
    c = a + b
    a = b
    b = c


# 38 A user enters a number such as 4826. Reverse the digits to produce 6284.

num = int(input("Enter a number :"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number :",reverse)


# 39 A perfect number equals the sum of its positive factors excluding itself. Check whether a number is perfect.

num = int(input("Enter a number :"))
total = 0

for i in range(1,num):
    if num % i == 0:
        total = total + i

if total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# 40 A user enters a number. Calculate the sum of its digits.

num = int(input("Enter a number :"))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of Digits :",total)


# 41 A shopping cart contains several product prices. Calculate the total bill and count items costing more than ₹500.

total = 0
count = 0

for i in range(1,6):
    price = int(input("Enter product price :"))
    total = total + price
    if price > 500:
        count = count + 1

print("Total Bill :",total)
print("Items Above ₹500 :",count)


# 42 A teacher enters marks for 10 students. Count passes and failures and calculate the class average. Passing marks are 35.

total = 0
passed = 0
failed = 0

for i in range(1,11):
    marks = int(input("Enter marks :"))
    total = total + marks

    if marks >= 35:
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed Students :",passed)
print("Failed Students :",failed)
print("Class Average :",total/10)


# 43 An ATM needs to calculate the number of ₹500, ₹200 and ₹100 notes required for a withdrawal amount.

amount = int(input("Enter withdrawal amount :"))

notes500 = amount // 500
amount = amount % 500

notes200 = amount // 200
amount = amount % 200

notes100 = amount // 100
amount = amount % 100

print("₹500 Notes :",notes500)
print("₹200 Notes :",notes200)
print("₹100 Notes :",notes100)
print("Remaining Amount :",amount)


# 44 An electricity company charges different rates for different ranges of units consumed. Calculate the bill.

units = int(input("Enter units consumed :"))

if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units-100) * 5
else:
    bill = 100 * 3 + 100 * 5 + (units-200) * 7

print("Electricity Bill :",bill)


# 45 A person records expenses for 30 days. Calculate the total, average and highest expense.

total = 0
highest = 0

for i in range(1,31):
    expense = int(input("Enter daily expense :"))
    total = total + expense

    if expense > highest:
        highest = expense

print("Total Expense :",total)
print("Average Expense :",total/30)
print("Highest Expense :",highest)


# 46 A login system allows a maximum of 3 attempts. Stop when the correct password is entered or attempts are exhausted.

correct_password = "python123"

for i in range(1,4):
    password = input("Enter password :")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect Password")

else:
    print("Attempts Exhausted")


# 47 A teacher wants a multiplication grid for numbers 1 through 10.

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()


# 48 A user enters the number of rows. Print a pattern where each row contains consecutive numbers starting from 1.

rows = int(input("Enter number of rows :"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


# 49 A user enters a positive integer. Display its digit count, digit sum, reversed number and whether it is a palindrome.

num = int(input("Enter a positive number :"))
original = num
temp = num
count = 0
total = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    count = count + 1
    total = total + digit
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Digit Count :",count)
print("Digit Sum :",total)
print("Reversed Number :",reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 50 A teacher enters marks for multiple students. Calculate each percentage, assign a grade and display the class average.

students = int(input("Enter number of students :"))
total = 0

for i in range(1,students+1):
    marks = int(input("Enter marks out of 100 :"))
    total = total + marks

    print("Student",i,"Percentage :",marks,"%")

    if marks >= 90:
        print("Grade : A")
    elif marks >= 75:
        print("Grade : B")
    elif marks >= 60:
        print("Grade : C")
    elif marks >= 35:
        print("Grade : D")
    else:
        print("Grade : F")

if students > 0:
    print("Class Average :",total/students)    