import random

question = raw_input("Ask the magic 8 ball a question: ")

answers = ["It is certain", "Outlook good", "You may rely on it", "Ask again later",
"Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]

valid = False

def find_element_in_string(element, string):
    try:
        index_element = string.index(element)
        return index_element
    except ValueError:
        return None

while valid != True:
    valid = True
    if question == "":
        valid = False
        print "Ask your question!"
        question = raw_input("Ask the magic 8 ball a question: ")
    elif find_element_in_string("?", question) >= 0:
        ansInt = random.randint(0,7)
        print answers[ansInt]
    else:
        valid = False
        print "Was that a question?"
        question = raw_input("Ask the magic 8 ball a QUESTION: ")
