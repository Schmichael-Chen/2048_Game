#!/usr/bin/python

'''

Copyright (c) 2014 Schmichael Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Schmichael Chen <schchen2000@yahoo.com>

'''

import global_variables

from random import randint

from is_game_over import is_game_over

def populate_game_board_with_new_seed():

	if is_game_over() == "Yes":

		return "Failure"

	while True:

		global_variables.game_board_newest_seed_index = randint(0,15)

		if global_variables.game_board[global_variables.game_board_newest_seed_index] == 0:
				
			break

	while True:

		global_variables.game_board[global_variables.game_board_newest_seed_index] = randint(2, 4)

		if global_variables.game_board[global_variables.game_board_newest_seed_index] != 3:

			break	

	if global_variables.game_board[global_variables.game_board_newest_seed_index] != 3 and global_variables.game_board[global_variables.game_board_newest_seed_index] > 0:		

		return "Success"

	return "Failure"
