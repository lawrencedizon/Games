import random
import sys

roll = True
while roll:
    question = input("Ask the magic 8 ball a question: (Press enter to quit):")

    answer = random.randint(1,9)
    if question == "":
        sys.exit()
    elif answer == 1:
        print("It is certain")
    elif answer == 2:
        print("My sources say no")
    elif answer == 3:
        print("As I see it, yes")
    elif answer == 4:
        print("Ask again later.")
    elif answer == 5:
        print("Reply hazy, try again.")
    elif answer == 6:
        print("Without a doubt.")
    elif answer == 7:
        print("Cannot predict now.")
    elif answer == 8:
        print("Ask again later.")
    elif answer == 9:
        print("Don’t count on it.")



