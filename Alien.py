class Alien :
    def __init__(self, name, legs, skin, height):
        self.name = name
        self.legs = legs
        self.skin = skin
        self.height = height

    def introduction(self):
        print(f"My name is {self.name}, i have {self.legs} legs, my skin is {self.skin} and i am {self.height} feet tall")
    def isTired():
        Tired = True
    def eat(self):
        if(self.legs == 2):
            print(f"{self.name} can't eat his last 2 legs")
        else:
            self.legs = self.legs - 1
            print(f"{self.name} ate his leg and has {self.legs} left!")
    def regenerate(self):
        self.legs = self.legs + 1
        print(f"{self.name} regenerated 1 leg")
    def fly(isTired):
        if(Tired == True):
            print("{self.name can't fly, he is tired}")
        else:
            print(f"{self.name} flied across the planet 1 time")
            print(f"{self.name} is tired")
            Tired = True
        
    def sleep(self, isTired):
        print(f"{self.name} slept like a kitty")
        print(f"{self.name} is not tired")
        Tired = False

Alien1 = Alien("ZzSNAUnusa", 5, "green", 7)
Alien1.introduction()

Command = input("Tell ur alien what to do? (eat, sleep, fly, end journey) ")
while(Command != "end journey"):
    if (Command == "eat"):
        Alien1.eat()
    elif (Command == "sleep"):
        Alien1.sleep()
        Alien1.regenerate()
    elif (Command == "fly"):
        Alien1.fly()
        
    Command = input("Tell ur alien what to do? ")

Print(f"Alien journey has ended!")


