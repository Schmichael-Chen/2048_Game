#!/user/bin/python

'''

Copyright (c) 2014 Schmichael Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Schmichael Chen <schchen2000@yahoo.com>

'''

import global_variables

def is_game_over():

	vertical_index = 0

	horizontal_index = 0

	return_code = "None"
	
	# ++++++++++++++++++++++++++++++++++
	# Beginning of checking horizontally
	# ++++++++++++++++++++++++++++++++++

	while horizontal_index < 4:

		while vertical_index < 3:

			index = vertical_index + (horizontal_index * 4)

			if global_variables.game_board[index] == 0: # A number in a row is 0.

				return_code = "No"

				break

			else: # A number is NOT 0.

				if global_variables.game_board[index] == global_variables.game_board[index + 1]:
				# 2 adjacent numbers are not 0's and they are same numbers, i.e. the game can continue on.

					return_code = "No"

					break

				else:
				# 2 adjacent numbers are NOT the same. global_variables.game_board[index] is NOT 0 but global_variables.game_board[index + 1] can be a 0 or a different number from global_variables.game_board[index].

					if global_variables.game_board[index + 1] == 0:

						return_code = "No"

						break

					else:
					# global_variables.game_board[index + 1] != 0 AND global_variables.game_board[index] != global_variables.game_board[index + 1]

						vertical_index += 1 # while vertical_index < 3:

		if return_code != "None":

			break

		vertical_index = 0 # Resetting for another inner while loop
																		
		horizontal_index += 1 # while horizontal_index < 4:

	# ++++++++++++++++++++++++++++
	# End of checking horizontally
	# ++++++++++++++++++++++++++++

	if return_code == "None": # Continue on with checking vertically

		vertical_index = 0

		horizontal_index = 0		

		# ++++++++++++++++++++++++++++++++
		# Beginning of checking vertically
		# ++++++++++++++++++++++++++++++++	

		while vertical_index < 4:

			while horizontal_index < 3: 

				index = vertical_index + (horizontal_index * 4)

				if global_variables.game_board[index] == 0: # A number in a row is 0.

					return_code = "No"

					break

				else: # A number is NOT 0.

					if global_variables.game_board[index] == global_variables.game_board[index + 4]:
					# 2 adjacent numbers are not 0's and they are same numbers, i.e. the game can continue on.

						return_code = "No"

						break

					else:
					# 2 adjacent numbers are NOT the same. global_variables.game_board[index] is NOT 0 but global_variables.game_board[index + 4] can be a 0 or a different number from global_variables.game_board[index].

						if global_variables.game_board[index + 4] == 0:

							return_code = "No"

							break

						else:
						# global_variables.game_board[index + 4] != 0 AND global_variables.game_board[index] != global_variables.game_board[index + 4]

							horizontal_index += 1 # while horizontal_index < 3:

			if return_code != "None":

				break

			horizontal_index = 0 # Resetting for another inner while loop
																		
			vertical_index += 1 # while vertical_index < 4:
		
		# ++++++++++++++++++++++++++
		# End of checking vertically
		# ++++++++++++++++++++++++++

	else: # if return_code != "None"

		return return_code

	if return_code == "None":

		return "Yes"

	else:

		return return_code
