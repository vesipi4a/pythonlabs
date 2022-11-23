str=input("Въведете низ: ")
str1=str*2
print(f"Удвоеният низ е {str1}")
add=input("Въведете втори низ: ")
str2=str+add 
print(f"Конкатенираните низове са {str2}")
for i in range(0,len(str)): 
    print(str[i])
fstr=input("Въведете търсен подниз: ")
n=str.find(fstr) 
if n!=-1:
    print(f"{fstr} е на позиция {n} в низа {str}")
else:
    print(f"{fstr} не се среща в низа{str}")
sstr = input("Въведете низ, който искате да замените")
if sstr == str:
    kude = input("Къде?: ")
    zamqna = input("Заменете низ: ")
    m = str.replace(kude, zamqna)
    print(m)
elif sstr == add:
    kude = input("Къде?: ")
    zamqna = input("Заменете низ: ")
    m = add.replace(kude, zamqna)
    print(m)
else:
    print("Не е намерен низ!")

