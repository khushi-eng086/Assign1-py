# # Restaurant Tip Simulator:

# # Get the bill amount from user
# bill_amount = float(input("Enter the total bill amount: $"))

# # Get the number of people to split the bill
# num_friends = int(input("Enter number of friends to split the bill: "))

# tip_percent = float(input("Enter tip percentage (10 to 50): "))

# if tip_percent < 10 or tip_percent > 50:
#     print("Invalid tip percentage. Please enter a value between 10 and 50.")
# else:
#     # Calculate tip and total amount
#     tip_amount = (tip_percent / 100) * bill_amount
#     total_amount = bill_amount + tip_amount

#     per_person_amount = total_amount / num_friends

#     print(f"\n--- Bill Summary ---")
#     print(f"Original Bill: ${bill_amount:.2f}")
#     print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
#     print(f"Total Amount (with Tip): ${total_amount:.2f}")
#     print(f"Each Person Pays: ${per_person_amount:.2f}")





# # Simple Calculator using if-else

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # Using if-else:
# if operator == "+":
#     result = num1 + num2
#     print(f"Result: {num1} + {num2} = {result}")
# elif operator == "-":
#     result = num1 - num2
#     print(f"Result: {num1} - {num2} = {result}")
# elif operator == "*":
#     result = num1 * num2
#     print(f"Result: {num1} * {num2} = {result}")
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print(f"Result: {num1} / {num2} = {result}")
#     else:
#         print("Error: Cannot divide by zero.")
# else:
#     print("Invalid operator. Please choose +, -, *, or /.")




# # Define the functions
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Cannot divide by zero"
#     return a / b

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # operation using function calls
# if operator == "+":
#     result = add(num1, num2)
# elif operator == "-":
#     result = subtract(num1, num2)
# elif operator == "*":
#     result = multiply(num1, num2)
# elif operator == "/":
#     result = divide(num1, num2)
# else:
#     result = "Invalid operator."

# print("Result:", result)
    
    
    