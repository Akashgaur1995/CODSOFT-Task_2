x=float(input("Enter First Number: "))
y=float(input("Enter Second Number: "))
z=str(input("Select Operator (+,-,*,/): "))
if z== '+':
    print("Addition is: ", x+y)
elif z== '-':
    print("Substraction is: ", x-y)
elif z== '*':
    print("Multiplication is: ", x*y)
elif z== '/':
    print("Division is: ", x/y)
else:
    print("Wrong operator")