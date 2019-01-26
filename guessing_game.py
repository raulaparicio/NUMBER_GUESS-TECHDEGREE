"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""


import sys
import random
def start_game():
  numberOfGuesses = 0
  number = random.randint(1,10)
  round(number)
  while True:
    try:
      guess = int(input("Choose a number between 1 and 10: "))

      numberOfGuesses += 1
      if (guess < number):
        print("Too low!")
      elif (guess > number):
        print("Too high!")
      elif (guess == number):
        print("Perfect!you guessed it in " + str(numberOfGuesses) + " guesses. Good Work")
        print("Ready to close")



        break
    except ValueError:
      print("Sorry you must enter a number")


    # write your code inside this function.
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    print("""
----------------------------------------
 Welcome to the Number Guessing Game!
----------------------------------------
  """)
    start_game()
