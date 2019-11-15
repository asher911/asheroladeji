 #imports important stuff and sheep classes
import pickle
import random
import time
from pink_sheep import *
from black_sheep import *
from white_sheep import *
from login import *

#creates coins and hay values so they can be used later on
coins = 50
hay = 25

#creates field class which manages all 
class Field:
    """Simulate a field that can contain animals and crops"""

    #constructor for field. has list to store the different sheep
    def __init__(self,max_sheeps):
        self._sheeps = []
        self._max_sheeps = max_sheeps
        #max sheeps makes sure there is a limit of sheep you can have
        
    #function for creating sheep within the limit (the true allows another function to check if it was successful)
    def print_sheep(self,sheep):
        if len(self._sheeps) < self._max_sheeps:
            self._sheeps.append(sheep)
            return True
        else:
            return False

    # function for removing sheep("when they are sold")
    def remove_animal(self,position):
        return self._sheeps.pop(position)

    #function for reporting the state of sheep in the field
    def report_contents(self):
        sheep_report = []
        for sheep in self._sheeps:
            sheep_report.append(sheep.report())

        return {"Sheeps you have ": sheep_report}

    def report_names(self):
      sheep_names = []
      nn = 0
      for sheep in self._sheeps:
        animal = self._sheeps[nn]
        names = animal.report()["name"]
        sheep_names.append(names)
        nn += 1

      return{"Sheep you have":sheep_names}

    #function for feeding sheep
    def feed(self,food):
        #global imports the global value of hay
        global hay
 
        print("Enter the name of the sheep you want to feed.")
        naming = input("")
        #this for loop checks if the name is a valid name
        for b in range(0,len(self._sheeps)):
            t = b - 1
            animal = self._sheeps[t]
            if animal.report()["name"] == naming :
                #these if statements check if they have enough hay to feed the sheep and if the hay is more than the grass need
                if food <= hay:
                    if animal.needs()["Grass need"] <= food:
                        animal.grow(food)
                        hay = hay - food
                        print("Sheep fed")
                    else:
                        print("Sheep requires more hay than that.")
                        print(animal.needs()["Grass need"])
                else:
                    print("You don't have enough hay.")
                break
            elif (animal.report()["name"] != naming) and b == len(self._sheeps):
                print("I didn't recognise that name.")
                #this is called if thename is invalid
        
    #this function checks the value of a sheep and returns the cost so it can be sold
    def check_value(self,name):
        #might need to change this so it uses name instead of position
        numbs = 0
        for i in range(0,len(self._sheeps)):
            animal = self._sheeps[numbs]
            if name == animal.report()["name"]:
                return numbs
            elif (name != animal.report()["name"]) and numbs == len(self._sheeps):
                return ("bro")
            else:
                numbs += 1
                

    def get_value(self,position):
        animal = self._sheeps[position]
        if animal.report()["type"] == "Pink Sheep":
            if animal.report()["status"] == "Chunky boi":
                cost = 400
            if animal.report()["status"] == "Big boi":
                cost = 200
            if animal.report()["status"] == "lil lamb":
                cost = 150
            if animal.report()["status"] == "baby boi":
                cost = 100
            else:
                cost = 70
            print("Good")
        elif animal.report()["type"] == "Black Sheep":
            if animal.report()["status"] == "Chunky boi":
                cost = 500
            if animal.report()["status"] == "Big boi":
                cost = 400
            if animal.report()["status"] == "lil lamb":
                cost = 275
            if animal.report()["status"] == "baby boi":
                cost = 150
            else:
                cost = 100
            print("Good")
        else:
            if animal.report()["status"] == "Chunky boi":
                cost = 110
            if animal.report()["status"] == "Big boi":
                cost = 70
            if animal.report()["status"] == "lil lamb":
                cost = 40
            if animal.report()["status"] == "baby boi":
                cost = 25
            else:
                cost = 15
            print("Good")

        return cost
            
        
        
#growth function that cqalls the feed 
def grow(self):
    global hay 
    print()
    print("Hay:",hay)
    print("For growth - Black sheep need 5 . Pink sheep need 2. White sheep need 1")
    print("How much hay do you want to use[1 - 10].")
    #this [try] is more efficient than just ifs cus it keeps the program running if the user enters an invalid value
    optionValid = False
    while optionValid == False:
        try:
            foof = int(input('Enter value: '))
            if (foof >= 1) and (foof <= 10):
                print("Which sheep do you want to feed.")
                print(self.report_names())
                self.feed(foof)
                optionValid = True
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')

    menu(self)

#menu(self) just takes the user back to the main menu

#function for buying sheep and hay
def buy(self):
    global coins
    global hay
    print()
    print("1. Hay              (2 coins)")
    print("2. White Sheep      (10 coins)")
    print("3. Pink Sheep       (60 coins)")
    print("4. Black Sheep      (100 coins)")
    print("0. Back             ")
    print()
    print("Select an option to buy (",coins,"coins available )")
    #used in the while loop later on 
    cost = [0,2,10,60,100]
    buyed = 0
    optionValid = False
    
    while optionValid == False:
        try:
            buyed = int(input("Option selected: "))
            #checks if option is valid and if they can afford what they picked
            if (buyed >= 1) and (buyed <= 4):
                if coins > cost[buyed]:
                    print("Processing...")
                    coins = coins - cost[buyed]
                    optionValid = True
                else:
                    print("You cannot afford that.")
                    menu(self)
                    optionValid = True
            elif buyed == 0:
                #o just takes you back to the main menu 
                menu(self)
                optionValid = True
            else:
                print("Pleas enter a valid option")
        except ValueError:
            print("Pleas enter a valid option")

    #now the actual buying takes place
    if buyed == 1:
        hay += 1
        print("You now have",hay,"hay stacks")
        #asks user if they want more hay(reply no if you just don't want any)
        more_hay = input("How many more hay stacks do you want: ")
        if int(more_hay * 2) <= (coins):
            hay += int(more_hay)
            more_hay = int(more_hay) * 2
            coins = coins - more_hay
            print("Purchase complete")
            menu(self)
        else:
            print("Sadly you cannot afford",(more_hay + 1),"hay stacks")
            menu(self)
    elif buyed == 2:
        named = input("What will you name it: ")
        if self.print_sheep(White(named)):
            print("Purchase complete.")
            menu(self)
        else:
            print("You've reached your sheep limit. Sell some to make space in the pit.")
            menu(self)
    elif buyed == 3:
        named = input("What will you name it: ")
        if self.print_sheep(Pink(named)):
            print("Purchase complete.")
            menu(self)
        else:
            print("You've reached your sheep limit. Sell some to make space in the pit.")
            menu(self)
    elif buyed == 4:
        named = input("What will you name it: ")
        if self.print_sheep(Black(named)):
            print("Purchase complete.")
            menu(self)
        else:
            print("You've reached your sheep limit. Sell some to make space in the pit.")
            menu(self) 


    #now buy stuff


#the function that shows what exactly the user owns 
def inventory(new_field):
    print()
    print("-        Your inventory         -")
    print("Coins: ",coins)
    print("Hay: ", hay)
    print(new_field.report_contents())
    time.sleep(2)
    menu(new_field)

#the quiz game for making money
def gamer(self):
    global coins
    #score is for storing the score(duh) and x and y are for randomising the opening question
    score = []
    x = int((random.random() *10))
    y = int((random.random() * 10))
    
    print()
    print("Opening question(2 points)")
    #I know. basic question that's different everytime. feel free to marvel at my genius
    print("If you have",x,"sheep and each of them needs",y,"stacks of hay. How much hay do you need altogether")
    ans1 = input("Answer: ")
    
    if int(ans1) == (x*y):
        print("That's...    Right.")
        score.append(1)
        #these list stores the questions and answers
        quiz = ["What is a young sheep called?","Does sheep wool grow forever","What is the shape of a sheep's pupil?","Sheep wool is harvested by doing what",
                "What is a female sheep called?","What is an adult sheep meat called?","What is a group of sheep called(apart from flock)?","Hay is a type of: ",
                "Which country has the largest number of sheep? ","What are male sheep called? "]
        quiz_ans = ["lamb","ye","rect","shear","ewe","mutton","herd","peren","china","ram"]
        #perfect answers that are show if a person gets a question wrong
        true_ans = ["lamb","yes","rectangular","shearing","ewe","mutton","herd","perennial crop","china","ram"]

        b = 11
        #for loop gives question 3 times
        for dd in range(0,3):
            a = int((random.random() *9)) - 1
            #if statement to ensure question isn't picked three times(still in the works)
            if a != b :
                print(quiz[a])
                your_ans = input("Your answer: ")
                if quiz_ans[a] in your_ans:
                    print("That's...    RIGHT.")
                    #increases length of score thus increasing the score
                    score.append(1)
                else:
                    print("Sorry the correct answer was",true_ans[a])
                b = a
            else:
                a += 1
                print(quiz[a])
                your_ans = input("Your answer: ")
                if quiz_ans[a] in your_ans:
                    print("That's...    RIGHT.")
                    score.append(1)
                else:
                    print("Sorry the correct answer was",true_ans[a])

        #turns points to coins
        coins = coins + (3 * len(score))
        menu(self)

    #if the opening question is answered wrong then you can't take the quiz now
    else:
        print("Sorry you lost the opening question.")
        menu(self)
        
#function for getting coins
def get_coins(self):
    global coins
    print()
    print("1. Take quiz")
    print("2. Gamble")
    print("3. Sell sheep")
    print("0. Back to main menu")
    print()
    wich = input("Option Selected: ")
    if int(wich) == 1:
        #calls quiz function
        gamer(self)
    elif int(wich) == 2:
        #just plays the gambling game so you can either win or lose or not change.
        print("Coins available:",coins)
        print("Capital is at risk. Play responsibly")
        wager = int(input("How much do you want to wager[1-20]: "))
        if (wager >= 1) and (wager <= 20) and (coins > wager):
            coins = coins - wager
            print("rolling...")
            luck = int(random.random() * 3)
            luck = (luck) * wager
            coins += luck
            time.sleep(3)
            print("You now have",coins,"coins")
            menu(self)
        elif coins > wager:
            print("That is not between 1 and 20")
            get_coins(self)
        else:
            print("You do have that many coins.")
            get_coins(self)
    elif int(wich) == 3:
        print(self.report_contents())
        sellin = input("What is the name of the sheep you want to sell: ")
        #call the pricing in the class and gets cost
        costly = self.check_value(sellin)
        if type(costly) is int:
            costlier = self.get_value(costly)
            self.remove_animal(costly)
            coins += costlier
            inventory(self)
        else:
            print("That name is invalid")
            menu(self)
        
    else:
        #got lazy so if you don't enter a valid option you just go back to the main menu 
        print("Back to main menu it is.")
        print()
        menu(self)

#function for instructions while playing the game            
def help_me(self):
    print("- Your duty is to raising the sheep by feeding it hay which you can buy from the store")
    print("- You can also buy and sell sheep")
    print("- The bigger the sheep you grow the more money you can sell it for")
    print("- To make money you can also play a quiz or gamble your coins")
    print("- You are starting with 50 coins, one sheep and 25 stacks of hay.")
    print("- When picking menu options, or a sheep's position in the list, use a number.")
    print()
    print("Good luck")
    ready = input("Is that ok ")
    menu(self)


    
        

# function for the main menu
def menu(new_field):
    print()
    print("1. Feed one sheep")
    print("2. Buy new sheep or hay")
    print("3. Get coins")
    print("4. See inventory")
    print("5. Help")
    print("0. exit Game")
    print()
    optionValid = False
    while optionValid == False:
        try:
            opt = int(input('Option Selected: '))
            if (opt >= 0) and (opt <= 5):
                optionValid = True
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')

    if optionValid == True:
        if opt == 0:
          asher = new_field.report_contents()
          pickle_out = open("dict.pickle","wb")
          pickle.dump(asher,pickle_out)
          pickle_out.close()
          exit()
        elif opt == 1:
          grow(new_field)
        elif opt == 2:
          buy(new_field)
        elif opt == 3:
          get_coins(new_field)
        elif opt == 4:
          inventory(new_field)
        elif opt == 5:
          help_me(new_field)


    
    
#this initialises the field and the creates the first sheep
def start():
    new_field = Field(10)
    print("Your first sheep has been created.")
    named = input("What will you name it: ")
    
    new_field.print_sheep(White(named))
    print(new_field.report_contents())
    menu(new_field)

#funtion for instructions before playing the game
def instructions():
    print("-----------------------This is a sheep raising pit---------------------------")
    print()
    print("- Your duty is to raising the sheep by feeding it hay which you can buy from the store")
    print("- You can also buy and sell sheep")
    print("- The bigger the sheep you grow the more money you can sell it for")
    print("- To make money you can also play a quiz or gamble your coins")
    print("- You are starting with 50 coins, one sheep and 25 stacks of hay.")
    print("- When picking menu options, or a sheep's position in the list, use a number.")
    print()
    print("Good luck")
    time.sleep(7)
    print()
    display_menu()

#function for first display menu
def display_menu():
    print("Press enter to start the game")
    print("Enter 0 for instructions")
    print()
    ans = input("")
    if ans == "0":
        instructions()
    else:
        start()
        
#this actually gets the game started(but only if this is the main program)
if __name__ == "__main__":
   display_menu()
