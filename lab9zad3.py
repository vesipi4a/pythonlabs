def sum(x=1,y=1):
    z = x+y
    return z
def dif(x=1,y=1):
    z = x-y
    return z
def product(x=1,y=1):
    z = x*y
    return z

a = float(input("a = "))
b = float(input("b = "))
print("Suma ot vuvedenite chisla")
rez=sum(a,b)
print(rez)
print("Suma samo s purvoto i podrazbirashto se chislo")
rez=sum(a)
print(rez)
print("Suma samo s vtoroto i podrazbirashto se chislo")
rez=sum(b)
print(rez)
print("Razlika ot vuvedenite chisla")
rez=dif(a,b)
print(rez)
print("Razlika s purvoto i podrazbirashto se chislo")
rez=dif(a)
print(rez)
print("Razlika s vtoroto i podrazbirashto se chislo")
rez=dif(b)
print(rez)
print("Proizvedenie ot vuvedenite chisla")
rez=product(a,b)
print(rez)
print("Proizvedebue samo s purvoto i podrazbirashto se chislo")
rez=product(a)
print(rez)
print("Proizvedebue samo s vtoroto i podrazbirashto se chislo")
rez=product(b)
print(rez)
