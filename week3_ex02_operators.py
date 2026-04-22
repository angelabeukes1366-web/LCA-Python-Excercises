# Question 1: Arithmetic and Assignment Operators
x = 10
y = 5

x += 3
result = x / y
print(x)
print(y *2)
print (result)

# Question 2: Comparison and Logical Operators
a = 8
b = 4
c = 6

condition1 = a > b
print(condition1)

condition2 = b % 2 ==0
print(condition2)

condition3 = c<= a
print(condition3)

a > b
final_condition = condition1 or (condition2 + condition3)
print(final_condition)

final_condition = condition1 or (condition2 and condition3)
print(final_condition)

# Question 3: Conditional Statements
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

elif score >= 60:
    grade = "D"

else: grade = "F"

print("Your grade is: " + grade)

# Question 4: Combining Operators and Conditionals

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2 

elif operation == "*":
    result = num1 * num2    

elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2

print("Result:", result)
