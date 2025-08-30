#BASIC GAME

import random
#x = int(input("ENTER LOWERBOUND : "))
#y = int(input("ENTER UPPERBOUND : "))
#z = int(input("ENTER YOUR GUESS: "))
#number = random.randint(x,y)
#if number == z:
#    print("CORRECT GUESS")
#else:
#    print("INCORRECT,TRY AGAIN!") 

#BETTER THAN BASIC

low = 0
high = 100
number =  random.randint(low,high)
guesses = 0
print("----NUMBER GUESSING GAME----")
print(f"ENTER A NUMBER BETWEEN {low} AND {high}")
while True:
    attempt = int(input("ENTER YOUR GUESS: "))
    guesses += 1
    if attempt < number:
       print("ENTER A GREATER NUMBER")
    elif attempt > number:
            print("ENTER A SMALLER NUMBER")
    else:
        print("WELL DONE!")
        print(f"YOU GUESSED THE NUMBER IN {guesses} CHANCE")