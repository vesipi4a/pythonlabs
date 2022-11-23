sum = 0
positive_numbers=0
while True:
    a= int(input("a= "))
    if a == -99:
        break
    if a<0:
        continue
    elif a>0:
        sum+=a
        positive_numbers+=1
print(f'sum = {sum} and positive numbers typed are {positive_numbers}')
    
