# Megan Mendez & Jazmeen De Gannes
# AP Computer Science Principle Create Task 2022
import random

print(
    "Welcome to Castle Roll\n\tIn this game you can roll (randomly draw a character) for Disney Characters using the "
    "set of commands listed below: \n"
    "- !r will roll characters from all available lists\n- !pr will roll Disney princesses\n- !s will roll special "
    "chosen characters \n- !v will roll Disney villans\n These commands are case sensitive. \n You will have a total "
    "of 6 turns to roll. Once the 6 turns are over, the game will end. However, you may terminate the game before the "
    "6 turns are over. \n"
)
name = input('To begin, choose a username: ')

prlist = [
    'Cinderella', 'Rapunzel', 'Jasmine', 'Mulan', 'Ariel', 'Tiana', 'Elsa',
    "Belle"
]  # this is the normal list
spedlist = [
    'Disgust', 'Wall-E', 'EVE', 'Dory', 'Mushu', 'Ursula', 'Bing Bong'
]  # this is the special list
villanlist = [
    'Maleficient', "Evil Queen", 'Jafar', 'Captain Hook', 'Scar', 'Ursula',
    'Mother Gothel'
]  # this is the villan list

roll = ""
turns = int(1)
# maybe have a limmit to the amount of rolls?
characters = ''
backpack = []


def rolllop():
    roll = input("\n Type Command: ")
    if roll == '!r':
        x = random.choices(
            prlist and spedlist
            and villanlist)  # this will draw a random string from either list
        characters = (x)
    elif roll == '!pr':
        y = random.choices(
            prlist)  # this will draw a random string from either list
        characters = (y)
    elif roll == '!s':
        z = random.choices(
            spedlist)  # this will draw a random string from either list
        characters = (z)
    elif roll == '!v':
        a = random.choices(villanlist)  # this will draw from the villan list
        characters = (a)
    elif roll != '!v' or '!r' or '!pr' or '!s':  # if an incorrect command is entered, then it will produce invalid and end the loop
        print("Command unavaliable, please try again")
    new = str(characters)
    print(
        str(name) + " you rolled, " + new + "."
    )  # need to add this input into a list that holds all the user's rolls
    backpack.append(characters)

def main():
    while turns <= 5:
        rolllop()
        turns = turns + 1
        another = input('Would you like to roll again? y or n: \n')
        # this code will repeat the individual roll sequence
        if turns == 6:
            print('\n You have one turn left \n')
        if another == 'y':
            rolllop()
            turns = turns + 1
            another = input('Would you like to roll again? y or n: \n')
        if another == 'n':
            print("Thank you for playing!")
            break  # will end the game if the player chooses to do so

    print("Hello " + str(name) + ","
                                 ' the characters in your castle are ' + str(backpack))

    # to end finally, it will list all the acquired characters they choose to keep.
    # thank you for playing.

if __name__== '__main__':
    main()
