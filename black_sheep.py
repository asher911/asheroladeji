#imports classes python
from classes import *

class Black(Buddy):
    """A black Sheep"""

    #constructor
    def __init__(self,name):
        #call the parent class constructor with default values for black sheep
        #growth rate = 1, food need = 6, 
        super().__init__(1,5,name)
        self._type = "Black Sheep"

    #override Buddy method for subclass grow
    def grow(self,grass):
        #make it so the sheep grows faster when younger
        while grass >= self._grass_need :
            if self._status == "smol boi" :
                self._growth += self._growth_rate * 1.25
                grass = grass - self._grass_need 
            elif self._status == "baby boi" :
                self._growth += self._growth_rate * 1.125
                grass = grass - self._grass_need 
            elif self._status == "lil lamb":
                self._growth += self._growth_rate * 1
                grass = grass - self._grass_need 
            else:
                self._growth += self._growth_rate * 0.8
                grass = grass - self._grass_need 



        #increment days growing and show status
        self._days_growing += 1
        self._update_status()


