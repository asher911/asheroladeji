import time
import sys
n = 0

def sign():
    # name and password is written unto the txt files in correct line
    name = input('Username: ')
    exist = False
    while exist == False:
      try:
        t = open('usernames.txt', 'r')
        exist = True
      except IOError:
        t = open('usernames.txt', 'w')
        t.write("a"+"\n")
        g = open('passwords.txt',"w")
        g.write("a"+"\n")
        t.close()
        g.close()

    t = t.read().splitlines()
    b = 0
    for a in range(0,len(t)):
      if name == t[b]:
        print('That username is already in use.')
        load_screen()
        break
      elif (name != t[b]) and (b == (len(t) - 1)):
        passed = input('Password: ')
        f = open('usernames.txt',"a+")
        f.write(name + "\n")
        f.close()
        g = open('passwords.txt',"a+")
        g.write(passed + "\n")
        g.close()
        print("You may now login.")
        asher = new_field.report_contents()
        pickle_out = open(name+".pickle","wb")
        pickle.dump(asher,pickle_out)
        pickle_out.close()
        time.sleep(1)
        load_screen()
        break
      else:
        b += 1

def passcheck():
  valid = False

  while valid == False:
    global n 
    username = input("Username: ")
    password = input("Password: ")
    user_note = open("usernames.txt","r")
    user_note = user_note.read().splitlines()
    y = int(len(user_note))
    n = 0

    for a in range(0,y):
      if user_note[n] == username:
        pass_note = open("passwords.txt","r")
        pass_note = pass_note.read().splitlines()
        if pass_note[n] == password:
          screen_code = "\033[2J";
          sys.stdout.write( screen_code )
          print("Login Successful !!!")
          return True
          valid = True
        else:
          print("Username or password incorrect.")
      elif (user_note[n] != username) and (n == y):
        print("Username does not exist")
      else:
        n += 1

def save_data():
  global n


def load_screen():
  print("1. Login")
  print("2. Create an account")
  print("0. exit")
  print()
  checked = False
  while checked == False:
    try:
      option = int(input("Option Selected: "))
      if (option >= 0) and (option <= 2):
        checked = True
      else:
        print("Please enter a valid option")
    except ValueError:
      print("Please enter a valid option")

  if option == 0:
    exit()
  elif option == 1:
    passcheck()
  elif option == 2:
    sign()

load_screen()