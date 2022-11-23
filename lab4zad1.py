sum = 0
n = int(input("How many numbers do you want to type? : "))
for i in range (0, n):
    a = int(input("Type a number: "))
    sum += a
print(f'sum = {sum}')
