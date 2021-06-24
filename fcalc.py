print("hello")
"""Design a calculator which will correctly solve all the problems except
   the following ones:  45 * 3 = 555, 56+9 = 77, 56/6 = 4
   Your program should take operator  and the two numbers as input from the user and then return the result.
"""
print("-----FAULTY CALCULATOR FOR SOME VALUES------\n")
print("enter your operator")
op = input("+,*,-,/")
a = int(input("enter first no."))
b = int(input("enter second no."))
#ADDITION
if op == "+":
  if a == 56:
   print("56+9=77")
  else:
    print(a+b)
#MULTIPLICATION
elif op == "*":
    if a == 45:
        print("45*3=555")
    else:
      print(a*b)
#DIVISION
elif op == "/":
    if a == 56:
        print("56/6=4")
    else:
       print(a/b)
#SUBSTRACTION
elif op == "-":
    print(a-b)

else:
    print("not defined")
