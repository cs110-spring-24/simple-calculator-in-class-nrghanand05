num1 = int(input ("Enter your first number: "))
operation = input ("Enter your operator: ")
num2 = int(input ("Enter your second number: "))

#ADDITION  
if operation == "+":
	total = num1 + num2 
	print(f"{num1} + {num2} = {total}")

#SUBTRACTION
elif operation == "-":
	print(f"{num1} - {num2} = {num1 - num2}")

#MULTIPLICATION
elif operation == "*":
	print(f"{num1} * {num2} = {num1 * num2}")

#DIVISION
elif operation == "/":
	if num2 == "0":
		print("Undefined.")
	else: 
		print(f"{num1} / {num2} = {num1 / num2}")

#POWER
elif operation == "**":
	print(f"{num1} ** {num2} = {num1 ** num2}")

#INTEGER DIVISON 
elif operation == "//":
	print(f"{num1} // {num2} = {num1 // num2}")

#MODULO
elif operation == "%":
	print(f"{num1} % {num2} = {num1 % num2}")


else: 
	print("Invalid, try another operation. Operations include: + Addition, - Subtration, * Multiplication, / Division, ** Power, // Integer Division, and % Modulo")





