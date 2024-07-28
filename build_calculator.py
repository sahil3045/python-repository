num1 = int(input(("Enter the first number: ")))
num2 = int(input(("Enter the second number: ")))
operator = input(("Enter the operator you want to use from + , -, *, /: "))

if operator == "+":
    print("The sum is: ", num1+num2)
elif operator =="-":
    print(("The difference is: ", num1-num2))
elif operator == "*":
    print("The product is: ", num1*num2)
elif operator == "/":
    print("The quotient is: ", int(num1/num2))
else:
    print("Invalid operator!")






