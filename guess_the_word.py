import os
import string
import random

os.system('clear')

with open("dictionary.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in open('dictionary.txt')]

def find_element_in_string(element, string):
    try:
        index_element = string.index(element)
        return index_element
    except ValueError:
        return None

choice = ""

# decide mode
while choice != "m" and choice != "r":
    choice = raw_input("Enter [m]ystery word or get [r]andom word: ").lower()
    os.system('clear')

if choice == "m":
    answer = raw_input("Input one secret word: ").lower()
    os.system('clear')
else:
    answer = (random.choice(lines))

# select how many guesses
guess_selected = False
chances = {"e": 7, "m": 5, "h": 3, "c": 1}
while guess_selected != True:
    print "Select mode:"
    print "[e]asy ----- 7 chances"
    print "[m]edium --- 5 chances"
    print "[h]ard ----- 3 chances"
    print "[c]razy ---- 1 chance"
    difficulty = raw_input("Input choice: ").lower()

    if find_element_in_string(difficulty, "emhc") == None:
        os.system('clear')
        print "Please enter valid selection!"
    else:
        guess_selected = True
        guesses_remaining = chances[difficulty]

valid_letters = string.lowercase

shown = ""
os.system('clear')

for letter in answer:
    shown+= ("_")


while guesses_remaining > 0:
    print "----- Letter Bank -----"
    print valid_letters
    print "-----------------------"
    print ""
    print shown
    print ""

    # checks if we have any more spaces we are looking for
    if find_element_in_string("_",shown) == None:
        print "Figured out word! Congratulations!"
        break

    print "Guesses Remaining: " + str(guesses_remaining)
    guess = raw_input("Guess a letter: ").lower()
    os.system('clear')

    # handles invalid inputs or already guessed letters
    if len(guess) > 1 or len(guess) == 0 or find_element_in_string(guess,valid_letters) == None:
        print "Please enter valid character"

    # replaces letters in shown word
    elif find_element_in_string(guess, answer) >= 0:
        print "Found a letter!"
        valid_letters = valid_letters.replace(guess, "")
        shown_arr = list(shown)
        answer_arr = list(answer)
        for count, elem in enumerate(answer_arr):
            if elem == guess:
                shown_arr[count] = guess
        shown = "".join(shown_arr)
        answer = "".join(answer_arr)

    # handles if letter is not in mystery word
    else:
        print "Letter doesn't exist"
        valid_letters = valid_letters.replace(guess, "")
        guesses_remaining-= 1


# handles game over
if guesses_remaining == 0:
    print "Secret word was: " + answer
    print "Sorry, you lose!"
