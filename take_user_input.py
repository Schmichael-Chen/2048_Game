#!/usr/bin/python

'''

Copyright (c) 2014 Schmichael Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Schmichael Chen <schchen2000@yahoo.com>

'''

# References
# ++++++++++

# 1) http://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments

import global_variables

from exit import exit

from new_game import new_game

from best_score import best_score

from current_score import current_score

from move_and_add_numbers import move_and_add_numbers

from initialize_game_board_and_print import initialize_game_board_and_print

def take_user_input(user_input):

	if user_input == "E":

		exit()

	elif user_input == "N":
		
		new_game()

		current_score()

		best_score()		

	elif user_input == "U" or user_input == "D" or user_input == "L" or user_input == "R": # Up, down, left & right

		move_and_add_numbers(user_input)	
