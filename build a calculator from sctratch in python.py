# Write a program to build a simple Calculator

# Available Operators
# 1. Addition (1): Sum of multiple numbers.
# 2. Subtraction (2): Difference between two numbers.
# 3. Division (4): Quotient of two numbers.
# 4. Average (5): Average of multiple numbers.

# 3 step Python program to create a simple calculator.

# 1. function for operation
# 2. user input
# 3. print result

# step 1: create function:

# function to add two numbers:

def add(num1, num2):
    return num1 + num2

# function to subract two numbers:

def sub(num1, num2):
    return num1 - num2


# function to multiple two numbers:

def mul(num1, num2):
    return num1 * num2

# function to divide two numbers:

def divide(num1, num2):
    return num1 / num2

# function to average two numbers:

def avg(num1, num2):
    return (num1 + num2) / 2

# step 2: user input

print("Please select a operation:\n "\
      "1. Addition\n "\
      "2. Subtraction\n "\
      "3. Multipication\n "\
      "4. Division\n "\
      "5. Average\n ")

select = int(input("Select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# step 3: Print the result:

if select == 1:
    print(number1, "+", number2, "= ", \
          add(number1, number2))


elif select == 2:
    print(number1, "-", number2, "= ", \
          sub(number1, number2))
    
elif select == 3:
    print(number1, "*", number2, "= ", \
          mul(number1, number2))
    
elif select == 4:
    print(number1, "/", number2, "= ", \
          divide(number1, number2))
    

elif select == 5:
    print("(",number1, "+", number2, ")", "/", "2", "= ", \
          avg(number1, number2))
    
else:
    print("Invaild operation!")