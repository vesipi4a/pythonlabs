x=input("Vuvedete chislo ot 1 do 7: ")
day1 ="ponedelnik"
day2 ="vtornik"
day3 ="srqda"
day4 ="chetvurtuk"
day5 ="petuk"
day6 ="subota"
day7 ="nedelq"
dni = ()
while(x != "END"):
    if x=='1':
        print(f'{x} = {day1}')
        dni = dni +(day1,)
    elif x=='2':
        print(f'{x} = {day2}')
        dni= dni + (day2,)
    elif x=='3':
        print(f'{x} = {day3}')
        dni=dni + (day3,)
    elif x=='4':
        print(f'{x} = {day4}')
        dni=dni+(day4,)
    elif x=='5':
        print(f'{x} = {day5}')
        dni=dni+(day5,)
    elif x=='6':
        print(f'{x} = {day6}')
        dni=dni+(day6,)
    elif x=='7':
        print(f'{x} = {day7}')
        dni=dni+(day7,)
    else:
        print("Chisloto e izvun granicata")
        break
    x = input("Vuvedete chislo ot 1 do 7 ")

print(dni)
