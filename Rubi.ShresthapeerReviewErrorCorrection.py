# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Rubi Shrestha -1
# Creation Date: 9/23/2020 -2
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.
# You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

# def chooseCave(): # #indention error -3


def chooseCave():      # after indention error correction
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
    # return caves (indention contains mixed places and tabs and also should be return cave instead of return caves) -4 & 5

	return cave  # after correction

def checkCave(chosenCave):
	print('You approach the cave...')
	# sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	# sleep for 2 seconds
	# time.sleep(3) (should be time.sleep(2) as per commented above sleep for 2 seconds) -6
	time.sleep(2)  # after correction
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	# sleep for 2 seconds
	time.sleep(2)
	friendly_cave = random.randint(1, 2)

	if chosenCave == str(friendly_cave):
		print('Gives you his treasure!')
	else:
		# print 'Gobbles you down in one bite!' # 'Goobles you down in one bite!' should be in parentheses -7
		print('Gobbles you down in one bite!')   # after correction


playAgain = 'yes'
# while playAgain = 'yes' or playAgain = 'y': (should be == after playAgain) -8

while playAgain == 'yes' or 'playAgain' == 'y':   # after correction
	displayIntro()
	# caveNumber = choosecave() # [choosecave() should be chooseCave()] -9
	caveNumber = chooseCave()   # corrected one
	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		# print("Thanks for planing")  # (should be playing instead of planing) -10
		print("Thanks for playing")  # (corrected one)


