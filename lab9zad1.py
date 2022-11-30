def pechat(start=0,end=10, inturn=1): # Функция за печат с два параметъра
    for i in range(start, end+1, inturn):
        print(f"{i}",end=" ")

st=int(input("Въведете начaло на интервала: ")) # Въвеждане на долна граница
stop=int(input("Въведете край на интервала: ")) # Въвеждане на горна граница
print(pechat.__doc__)
if st<stop: # Проверка за коректни граници на интервала
    print("Използване на подразбиращите се стойности: ")
    pechat() # start=0, end=10
    print("\nИзползване само на началната стойност:")
    pechat(st) # start=st, end=10
    print("\nИзползване само на крайната стойност:")
    pechat(0,stop) # start=0, end=stop
    print("\nИзползване на началната и крайната стойност:")
    pechat(st,stop) # start=st, end=stop
else:
    print("Некоректни граници!")
