from classes import *

class Pink(Buddy):
    """A pink sheep"""

    def __init__(self,name):
        super().__init__(1,2,name)
        self._type = "Pink Sheep"

    def grow(self,grass):
        
        while grass >= self._grass_need :
            if self._status == "smol boi" :
                self._growth += self._growth_rate * 1.5
                grass = grass - self._grass_need 
            elif self._status == "baby boi" :
                self._growth += self._growth_rate * 1.25
                grass = grass - self._grass_need 
            elif self._status == "lil lamb":
                self._growth += self._growth_rate * 1.12
                grass = grass - self._grass_need 
            else:
                self._growth += self._growth_rate * 1
                grass = grass - self._grass_need 

        self._days_growing += 1
        self._update_status()


    
