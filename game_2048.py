#!/usr/bin/python

'''

Copyright (c) 2014 Schmichael Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Schmichael Chen <schchen2000@yahoo.com>

'''

#=====================================================================================================

# References
# ++++++++++

# 1) http://stackoverflow.com/questions/13034496/using-global-variables-between-files-in-python 

#=====================================================================================================

import global_variables

from exit import exit

from __print__ import __print__

from best_score import best_score

from is_game_over import is_game_over

from score_update import score_update

from current_score import current_score

from percent_filled import percent_filled

from take_user_input import take_user_input

from can_score_be_updated import can_score_be_updated

from initialize_game_board_and_print import initialize_game_board_and_print

from populate_game_board_with_new_seed import populate_game_board_with_new_seed

def main():

	__print__("\nWelcome To 2048 Game")

	__print__("++++++++++++++++++++\n")

	__print__("Here is your game. Good luck, you!")

	initialize_game_board_and_print()

	current_score()

	best_score()

	user_input = "None"

	while True:

		global_variables.score_before_user_input = global_variables.score
		
		while True:
		
			print "\nType {U, D, L, R, N, E} to represent up, down, left, right arrow keys, new game & exit respectively.\n"

			user_input = raw_input("Enter your input: ") 
			
			if user_input == "U" or user_input == "D" or user_input == "L" or user_input == "R" or user_input == "N" or user_input == "E":
				break

			else:

				print "\nPlease re-enter your valid input."

				__print__("existing game board")

				current_score()

				best_score()

		take_user_input(user_input)

		if can_score_be_updated(global_variables.score_before_user_input) == "Yes":

			score_update()

			if populate_game_board_with_new_seed() == "Success":

				__print__("existing game board")	

				current_score()

				best_score()

		else:

			if user_input == global_variables.last_move:

				if percent_filled() >= 75:

					__print__("\nYour move is taking you nowhere. Make your new move in different directions.")

				elif percent_filled() < 75:

					if populate_game_board_with_new_seed() == "Success":

						__print__("existing game board")	

						current_score()

						best_score()

			else:

				#if global_variables.score != 0: 
				# Handling the case where the user has the same inputs and not making any progress

				if user_input != "N":

					if populate_game_board_with_new_seed() == "Success":

						__print__("existing game board")	

						current_score()

						best_score()

		global_variables.last_move = user_input # Updating last move			

		if is_game_over() == "Yes":

			__print__("\nGAME OVER!\n")

			break
	
main()
