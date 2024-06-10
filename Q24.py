Oper=input("Enter the operator (+,-,*,/): ")
num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
if Oper == "+":
    print("Sum of the two numbers is ",num1+num2)
elif Oper == "*":
    print("Product of the two numbers is ",num1*num2)
elif Oper == "-":
    print("Difference of the two numbers is ",num1-num2)
elif Oper == "/":
    print("Quotient of the two numbers is ",num1/num2)
else:
    print("Invalid")
