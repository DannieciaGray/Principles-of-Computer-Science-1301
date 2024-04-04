'''
Description: This code will write a number guessing game that generates a random number between 1 and 100. The player will
have only 10 attempts to guess the number through the terminal. After each guess by the player, the
game will need to provide feedback to the player about if their guess is greater than or less than the
random number.

Author: Danniecia
'''
# imports the random generator  
import random

# generates random number between 1 and 100
random_num=random.randint(1,100)

#Prompts the user 
print("I have generated random number between 1 and 100. You will have 10 attempts to guess that number.")

#allows the user to guess the number 10 times 
for i in range(1,11):
    guess=int(input(f"Guess {i}:"))
    if guess> random_num:
        print("Your guess is greater than my random number. Try Again.")
    elif guess < random_num:
         print("Your guess is less than my random number. Try Again.")
    elif guess == random_num:
        print("You correctly guessed my random number!")

        break  # stops generating guessing options if user gets correct answer 

# runs if user uses all attempts and enters the wrong answer.
else:
    print("You have run out of attempts! The correct answer was",random_num,".")

