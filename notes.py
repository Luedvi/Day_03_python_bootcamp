#conditional statements if/else
#if the condition in the "if" it's true, the indented code block is executed, otherwise the indented code block in the else will be executed, There's only 2 options for our code to follow
water_level=84
temperature=29
light=True

if water_level>80:
  print("stop pouring")
else:
  print("continue pouring")
#comparison operators:
# > greater than
# < less than
# >= greater or equal to
# <= less or equal to
# == equal to
# != not equal to

#the modulo operator "%"
#gives the remainder of a division e.g. 7/2=2*3 +1  or 47/5=5*9 +2
print(7%2)
print(47%5)
print(45%5)

#nested if/else
#once the first "if" condition is passed, the code checks for another set of conditions that are indented inside that "if"
if water_level>80:
  print("stop pouring")
  if temperature<20:
    print("the water is cold")
  else:
    print("the water is perfect")
else:
  print("continue pouring")

#elif statement
#we can have as many elif as we want between the "if" and "else" but once the code finds a true condition, it'll bypass the others, so the order in wich conditions are writen is important.
#you can omit the "else"
if temperature<=10:
  print("it's freezing cold")
elif temperature<=30:
  print("it's ok")
else:
  print("it's too hot")

#multiple "if" conditions
#if all conditions of all the "if" are true, then all the actions will be executed.
#if there's no actions to be executed in the "else" you can omit it
if water_level>80:
  print("stop pouring")
if temperature<=30:
  print("it's ok")
if light==True:
  print("let's get in")

#logical operators "and", "or", "not"
if water_level>80 and temperature<=30:
  print("both conditions have to be true")
if water_level>100 or temperature<=30:
  print("either one or both condition needs to be true")
if not light==False:
  print("it reverses a condition, if it's false it becomes true and viceversa")

#count () function gives you the number of times a letter occurs in a string and it's case sensitive
luis="LUIs EduaRdo VillEGaS urQuiZo"
letter_u=luis.count("u")
letter_U=luis.count("U")
print(letter_u)
print(letter_U)
#lower() function changes all the letters in a string to lower case.
luis_lower_case=luis.lower()
print(luis_lower_case)

characters="JACOBO GRINBERG"
letter_g=characters.lower().count("g")
print(letter_g)

#You can use three quotes ''' instead of two to create multiple lines of a string
print('''
                                ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\""--.:-.     `.                             .:/
                  \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                   `P         `-._ \          `-:\          `. `:\
                                   ""            "            `-._)
                                   ''')

#Escape characters
#To insert characters that are illegal in a string, use an escape character.An escape character is a backslash \ followed by the character you want to insert.

#\'	Single quote
print("this is an \"example\" of escape character")
#\\ backslash
print("this is an example of \\ backslash")
#\n new line
print("example of a \n new line")
#\r carriage return
print("this is an example of \r carriage return")
#\t tab
print("\t this is an example of tab")
#\b backspace
print("this is an example of back\bspace")
#\f form feed
print("this is an example\f of form feed")
#\000 A backslash followed by three integers will result in a octal value:
print("\110\145\154\154\157")
#\xhh A backslash followed by an 'x' and a hex number represents a hex value:
print("\x48\x65\x6c\x6c\x6f")
# short hand if: If you have only one statement to execute, you can put it on the same line as the if statement
a = 23
b = 27
if a > b: print("a is greater than b")

pokemon = input("choose a pokemon: pikachu, bulbasaur, squirtle, charmander")
if pokemon == "pikachu": print("the special starter pokemon")
elif pokemon == "charmander": print("love fire")
else: print("starter pokemon")

# short hand if/else: If you have only one statement to execute, one for if, and one for else, you can put it all on the same line. This technique is known as Ternary Operators, or Conditional Expressions.
print("a") if a > b else print("b")
# you can also have multiple "else" on the same line
print("A") if a > b else print("=") if a == b else print("B")

print("electric type") if pokemon == "pikachu" else print("grass type") if pokemon == "bulbasaur" else print("water type") if pokemon == "squirtle" else print("fire type") if pokemon == "charmander" else print("there are many types")
#ticket software example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120:
  print("you can ride the rollercoaster!")
  age=int(input("what is your age? "))
  if age<12:
    bill=5
    print("child tickets are $5")
  elif age<=18:
    bill=7
    print("youth tickets are $7")
  elif age>=45 and age<=55:
    bill=0
    print("middle age crisis ride for free")
  else:
    bill=12
    print("adult tickets are $12")
    
  photo=input("would you like a photo taken? y or n.")
  if photo=="y":
    bill+=3
  print(f"your final bill is ${bill}")
else:
  print("sorry, you have to grow taller before you can ride")

#https://ascii.co.uk/art
#https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
#https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
#https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
# https://www.w3schools.com/python/python_operators.asp
# https://www.w3schools.com/python/python_conditions.asp
