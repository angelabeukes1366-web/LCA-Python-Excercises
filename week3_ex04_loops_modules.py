# Question 1: Using a for loop with a list
fruits = ["Apple","Banana","Orange","Mango"]
for fruits in fruits :
    print(fruits)

# Question 2: Using a while loop for countdown
count = 5
while count >=1:
    print(count)
    count -= 1

# Question 3: Using a for loop with range()
for number in range(1,11) :
    square = number **2 
    print(square)

# Question 4: Using the random module
import random
colors = ["Red","Blue","Green","Yellow","Purple"]

for i in range (3):
    random_color = random.choice(colors)
    print(random_color)

# Question 5: Creating and using a custom module
 import math_operations

# Example usage
print(math_operations.add(5, 3))
print(math_operations.subtract(10, 4))
print(math_operations.multiply(6, 2))
print(math_operations.divide(8, 2))