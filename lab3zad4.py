x = int(input("Type a number: "))
y = int(input("Type a number: "))
Operation = input("Type operation (+, -, *, /)")
if (Operation == "+"):
    print(f'{x} + {y} = ',x+y)
elif (Operation == "-"):
    print(f'{x} - {y} = ',x-y)
elif (Operation == "*"):
    print(f'{x} * {y} = ',x*y)
elif (Operation == "/"):
    print(f'{x} / {y} = ', x/y)
else:
    print("undefined operation")
