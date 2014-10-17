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

# 1) http://stackoverflow.com/questions/5555712/generate-a-random-number

# 2) http://stackoverflow.com/questions/743164/do-while-loop-in-python

# 3) http://stackoverflow.com/questions/13034496/using-global-variables-between-files-in-python

#from global_variables import *

import global_variables

from __print__ import __print__

from random import randint

def initialize_game_board_and_print():

	global_variables.score = 0

	global_variables.last_move = "None"

	i = 0

	while i < 4:

		global_variables.place_holder[i] = 0

		i += 1

	i = 0

	while i < 16: # 16 is the total # of grids in the game board.

		global_variables.game_board[i] = 0

		i += 1

	global_variables.score_before_user_input = 0

	global_variables.game_board_first_seed_index = randint(0,15)

	while True:
	# This while loop simulates a do...while loop to ensure that 1st and 2nd seed indices are diferent.

		global_variables.game_board_second_seed_index = randint(0,15)

		if global_variables.game_board_first_seed_index != global_variables.game_board_second_seed_index:

			break

	game_board_newest_seed_index = 17 # Again, 17 is a sentinel value here.

	while True:
	# There is again a do....while loop simulation to ensure that both seed values are nothing but 2 & 4 and both values must be different.

		global_variables.game_board[global_variables.game_board_first_seed_index] = randint(2,4)

		global_variables.game_board[global_variables.game_board_second_seed_index] = randint(2,4)				

		if global_variables.game_board[global_variables.game_board_first_seed_index] != 3  and global_variables.game_board[global_variables.game_board_second_seed_index] != 3:

			if global_variables.game_board[global_variables.game_board_first_seed_index] == global_variables.game_board[global_variables.game_board_second_seed_index]:

				if global_variables.game_board[global_variables.game_board_first_seed_index] == 2:

					break

			else:

				break

	__print__("new game board")
