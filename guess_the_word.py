import os
import string
import random

os.system('clear')

with open("dictionary.txt") as f:
    content = f.readlines()

def find_element_in_string(element, string):
    try:
        index_element = string.index(element)
        return index_element
    except ValueError:
        return None

guesses_remaining = 5
valid_letters = string.lowercase
choice = ""

while choice != "m" and choice != "r":
    choice = raw_input("Enter [m]ystery word or get [r]andom word: ").lower()
    os.system('clear')


if choice == "m":
    answer = raw_input("Input one secret word: ").lower()
else:
    answer = (random.choice(content))


shown = ""
os.system('clear')

for letter in answer:
    shown+= ("_")


while guesses_remaining > 0:
    print "--- Letter Bank ---"
    print valid_letters
    print "-------------------"
    print shown

    if find_element_in_string("_",shown) == None:
        print "Figured out word! Congratulations!"
        break
    print "Guesses Remaining: " + str(guesses_remaining)
    guess = raw_input("Guess a letter: ").lower()
    os.system('clear')

    if len(guess) > 1 or len(guess) == 0 or find_element_in_string(guess,valid_letters) == None:
        print "Please enter valid character"
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
    else:
        print "Letter doesn't exist"
        valid_letters = valid_letters.replace(guess, "")
        guesses_remaining-= 1

if guesses_remaining == 0:
    print "Secret word was: " + answer
    print "Sorry, you lose!"
