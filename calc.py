num1 = float(input("Enter your first number: "))
op = input("Enter the opeartor(symbol) of choice: ")
num2 = float(input("Enter the second number: ")) 

if op == "+":
  print(num1+num2)
elif op == "-":
  print(num1-num2)
elif op == "*":
  print(num1*num2)
elif op == "/":
  print(num1/num2)
else :
 print("Invalid operator!")
