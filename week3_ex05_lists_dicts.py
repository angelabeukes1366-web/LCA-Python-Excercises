# Question 1: Creating and Modifying Lists
fruits = ["apple","banana","orange"]
fruits.append("grape")
fruits.insert(0,"mango")
fruits.remove ("banana")
print(fruits)

# Question 2: List Operations
numbers = [1,2,3,4,5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num**2)
total = sum(numbers)
average = total/len(numbers)
print("Original numbers:",numbers)
print("Squared numbers:",squared_numbers)
print("Sum",total)
print("Average:",average)

# Question 3: Creating and Modifying Dictionaries
countries = {       
    "South Africa" : "Pretoria",
    "France" : "Paris",
    "Japan" : "Tokyo"
}
countries["Germany"] = "Berlin"
countries["South Africa"] = "Cape Town"
countries.pop("France")
print(countries)

# Question 4: Dictionary Operations
fruit_colors = {
    "apple" : "red",
    "banana" : "yellow",
    "grape" : "purple"
}
print ("Fruits:",fruit_colors.keys())
print("Colors:",fruit_colors.values())
for fruit,color in fruit_colors.items():
    print(fruit,"is",color)
fruit_to_check = "apple"
if fruit_to_check in fruit_colors:
    print(fruit_to_check, "color is", fruit_colors[fruit_to_check])
else:
    print("Fruit not found")
