total=0
num1=float(input("enter a number"))
opp= input("enter an operator")
num2= float(input("enter a number"))
if opp == "+":
    total= num1 + num2
elif opp == "-":
    total= num1- num2
elif opp == "*":
    total= num1*num2
elif opp == "/":
    total= num1/num2
else:
      print("syntax error")
print("result is", total)
print (round(total,-1))

