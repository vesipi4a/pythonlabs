sum = 0
index = 0
while index<10:
    a = int(input("Type number: "))
    sum+=a
    index+=1

if (sum % 2 == 0):
    print(f'sum = {sum} and its even')
else:
    print(f'sum = {sum} and its odd')
