#!/usr/bin/python

'''

Copyright (c) 2014 Schmichael Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Schmichael Chen <schchen2000@yahoo.com>

'''

# To print game board, score & highest score

# References
# ++++++++++

# 1) https://pypi.python.org/pypi/colorama

# 2) http://ubuntuforums.org/showthread.php?t=840225 

# 3) http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

import math

from sys import stdout

from termcolor import colored

import global_variables

def __print__(what_to_print):

	if what_to_print != "new game board" and what_to_print != "existing game board":

		print what_to_print

	else:# Print new & existing game boards

		index = 0 # Will be used to index into each grid in the game board

		max_game_board_length = 0
		# This is the length of the rows. The length is determined by adding white spaces, asterisks and numberical digits to be displayed. The row of the game board with the largest numerical value will determine this length.

		largest_number_in_the_game_board = 0

		number_of_digits_in_the_largest_number_in_the_game_board = 0

		number_of_empty_spaces_flanking_a_number_in_game_board = 6

		number_of_demarcation_asterisks_per_row = 5

		while index < 16: # 16 is the total # of grids in the game board.
			
			if global_variables.game_board[index] > largest_number_in_the_game_board:

				largest_number_in_the_game_board = global_variables.game_board[index]

			index += 1 # while index < 16

		# Note: Instead of the following if....elif statements, I could possibly use the approach from here: 
		# http://stackoverflow.com/questions/2189800/length-of-an-integer-in-python

		if largest_number_in_the_game_board < 10:
		# 1-digit number

			max_game_board_length = 1

			number_of_digits_in_the_largest_number_in_the_game_board = 1

		elif largest_number_in_the_game_board >= 10 and largest_number_in_the_game_board < 100:
		# 2-digit number

			max_game_board_length = 2

			number_of_digits_in_the_largest_number_in_the_game_board = 2

		elif largest_number_in_the_game_board >= 100 and largest_number_in_the_game_board < 1000:
		# 3-digit number

			max_game_board_length = 3

			number_of_digits_in_the_largest_number_in_the_game_board = 3

		elif largest_number_in_the_game_board >= 1000 and largest_number_in_the_game_board < 10000:
		# 4-digit number

			max_game_board_length = 4

			number_of_digits_in_the_largest_number_in_the_game_board = 4

		elif largest_number_in_the_game_board >= 10000 and largest_number_in_the_game_board < 100000:
		# 5-digit number

			max_game_board_length = 5

			number_of_digits_in_the_largest_number_in_the_game_board = 5

		max_game_board_length += number_of_empty_spaces_flanking_a_number_in_game_board

		max_game_board_length *= 4 # x 4 because 4 grids / row

		max_game_board_length += number_of_demarcation_asterisks_per_row

		stdout.write('\n')

		index = 0

		while index < max_game_board_length: 
		# This while loop prints asterisks for the game board's upper boundary.

			stdout.write('*')

			index += 1 # while index < max_game_board_length

		lateral_index = 0 
		# This is the index(0....3) to go through the game board sideways.

		vertical_index = 0 
		# This is the index(0....3) to go through the game board vertically.

		while vertical_index < 4:

			print '\n'

			stdout.write('*')

			index = vertical_index * 4
			# Beginning index of each row

			while lateral_index < 4:

				running_index = index + lateral_index 
				# Making running index to be between 0 and 15 inclusive to map the grids in the entire board.

				stdout.write("   ") # 3 white spaces before each number

				if global_variables.game_board[running_index] > 0: # Print any number > 0

					if what_to_print == "new game board":

						if running_index == global_variables.game_board_first_seed_index or running_index == global_variables.game_board_second_seed_index:

                                                	print colored(global_variables.game_board[running_index], 'yellow'),

                                        	else:

                                                	print global_variables.game_board[running_index],
											
					elif what_to_print == "existing game board":

						if global_variables.game_board_newest_seed_index == 17:

							if global_variables.game_board_first_seed_index != 0 or global_variables.game_board_second_seed_index != 0:

								if running_index == global_variables.game_board_first_seed_index or running_index == global_variables.game_board_second_seed_index:

                                                        		print colored(global_variables.game_board[running_index], 'yellow'),

								else:

									print global_variables.game_board[running_index],		

						else:

							if running_index == global_variables.game_board_newest_seed_index:

                                                        	print colored(global_variables.game_board[running_index], 'yellow'),

							else:

								print global_variables.game_board[running_index],	

					i = 0 
					# Beginning of printing empty space(s) as compensation for numbers with smaller number of digits
					# i.e. if the largest # has 3 digits and the current # being printed has only 2 digits, then one empty space will be printed to compensate.

					count = number_of_digits_in_the_largest_number_in_the_game_board - (int(math.log10(global_variables.game_board[running_index])) + 1)
					
					while i < count:

						stdout.write(" ")

						i += 1
					# Ending of printing empty space(s) as compensation for numbers with smaller number of digits
							
				elif global_variables.game_board[running_index] == 0: # Print a space when run into a zero. 	

					i = 0

					while i < number_of_digits_in_the_largest_number_in_the_game_board:

						stdout.write(' ')			

						i += 1
				
				stdout.write("   *")
				# 3 white spaces after each number & a closing demarcation asterisk

				lateral_index += 1 # while lateral_index < 4	

			print '\n'

			index = 0

			while index < max_game_board_length: 
			# This while loop prints asterisks for the lower boundary of each row.

				stdout.write('*')

				index += 1 # while index < max_game_board_length		

			lateral_index = 0

			vertical_index += 1 # while vertical_index < 4
