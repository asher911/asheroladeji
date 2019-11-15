import random
ranit = random.randint(0, 10)
#generates random number

class Buddy:
    """Sheeple"""

    #constructor
    def __init__(self, growth_rate, grass_need,named):
        #set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._grass_need = grass_need
        self._status = "smol boi"
        self._type = "Sheep"
        self._name = named

    #returns a dictionary containing needs
    def needs(self):
        return {"Grass need": self._grass_need}

    #method to return report on state of sheeples
    def report(self):
        return{"name":self._name,"type":self._type,"status":self._status,"growth":self._growth,"days growing":self._days_growing}

    #method to update status
    def _update_status(self):
        if self._growth >= 30:
            self._status = "Chunky boi"
        elif self._growth > 20:
            self._status = "Big boi"
        elif self._growth > 9:
            self._status = "lil lamb"
        elif self._growth > 0:
            self._status = "baby boi"
        else:
            self._status = "smol boi"

    #method that changes variables
    def grow(self,grass):
        while grass >= self._grass_need :
            self._growth += self._growth_rate
            grass = grass - self._grass_need

        grass = 0
        #update the game
        self._days_growing += 1

        self._update_status()

def auto_grow(Buddy, days):
    for day in range(days):
        hay = random.randint(1,10)
        Buddy.grow(hay)

def manual_grow(Buddy):
    hay = int(input("How much hay are you giving your sheep: "))
    Buddy.grow(hay)

    
def main():
    print("-------------------------------ASHER'S SHEEP------------------------------------")
    #instantiate the class(basically calling one)
    new_sheep = Buddy(1,3)
    #returns functions needs and report
    print(new_sheep.needs())
    print(new_sheep.report())

    auto_grow(new_sheep,30)
    print(new_sheep.report())
    #you can also return something specific
    print(new_sheep.report()["growth"])
    

if __name__ == "__main__":
    main()

