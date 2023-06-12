# Testing everything
### This is a calculator in spanish

# Prompt the user for input
print('Bienvenido a la calculadora de Martin')
print('¿Que necesitas calcular hoy?')
num1 = float(input("Primer numero a calcular: "))
num2 = float(input("Segundo numero a calcular: "))
operator = input("Seleciona el tipo de operación (+, -, *, /): ")

# Perform the mathematical operation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Operacion invalida!")

# Display the result
print("El resultado es:", result)
