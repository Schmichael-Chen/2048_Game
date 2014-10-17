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

# 1) http://www.i-programmer.info/programming/python/3942-arrays-in-python.html?start=1

from sys import stdout

import global_variables

from move_and_add import move_and_add

def move_and_add_numbers(direction):

	score = 0

	index = 0

	vertical_index = 0

	horizontal_index = 0

	if direction == "U":

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Beginning of populating the place_holder[] in the global_variables.py 
		# using one column of the game board at a time going from left to right
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		while vertical_index < 4: # 4 here is the total # of columns in the game board.

			while horizontal_index < 4: # 4 here is the total # of rows in the game board.

				index = vertical_index + (horizontal_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.place_holder[horizontal_index] = global_variables.game_board[index]
				# horizontal_index here runs from 0 .... 3 and using it with global_variables.place_holder[] would save me setting up a for loop running from 0 to 3. The topmost entry in a column of the game board maps into the leftmost entry of the place_holder[] in the global_variables.py.

				horizontal_index += 1	

			horizontal_index = 0 # This is done for the following while loop.

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# End of populating the place_holder[] in the global_variables.py using
		# one column of the game board at a time going from left to right
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			 
			move_and_add()
			# Add and move #'s inside the place_holder[] in the global_variables.py and move them to the low end of the array.

			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		
			# Copying the contents of the place_holder[] back into the appropriate
			# column, i.e. left to right of the place_holder[] would map into the
			# top to the bottom of the appropriate column of the game board.
			#
			# Note
			# ****
			# 
			# I only need one while loop as follows for while vertical_index < 4:
			# above can be reused.
			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
										
			while horizontal_index < 4: # 4 here is the total # of rows in the game board.

				index = vertical_index + (horizontal_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.game_board[index] = global_variables.place_holder[horizontal_index]
				# horizontal_index here runs from 0 .... 3 and using it with global_variables.place_holder[] would save me setting up a for loop running from 0 to 3.

				horizontal_index += 1	

			horizontal_index = 0
			# This is done in preparation for the above while horizontal_index < 4: # 4 here is the total # of rows in the game board.
			vertical_index += 1			

	elif direction == "D":

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Beginning of populating the place_holder[] in the global_variables.py 
		# using one column of the game board at a time going from left to right
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		while vertical_index < 4: # 4 here is the total # of columns in the game board.

			while horizontal_index < 4: # 4 here is the total # of rows in the game board.

				index = vertical_index + (horizontal_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.place_holder[3 - horizontal_index] = global_variables.game_board[index]
				# The topmost entry in a column of the game board maps into the rightmost entry of the place_holder[] in the global_variables.py.
				
				horizontal_index += 1	

			horizontal_index = 3 # This is done for the following while loop.

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# End of populating the place_holder[] in the global_variables.py using
		# one column of the game board at a time going from left to right
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			 
			move_and_add()
			# Add and move #'s inside the place_holder[] in the global_variables.py and move them to the low end of the array.

			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		
			# Copying the contents of the place_holder[] back into the appropriate
			# column, i.e. left to right of the place_holder[] would map into the
			# bottom to the top of the appropriate column of the game board.
			#
			# Note
			# ****
			# 
			# I only need one while loop as follows for while horizontal_index >= 0:
			# above can be reused.
			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
										
			while horizontal_index >= 0: 

				index = vertical_index + (horizontal_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.game_board[index] = global_variables.place_holder[3 - horizontal_index]
				# The leftmost entry of the place_holder[] would map into the lowest entry of a column in the game board.

				horizontal_index -= 1	

			horizontal_index = 0
			# This is done in preparation for the above while horizontal_index < 4: # 4 here is the total # of rows in the game board.
			vertical_index += 1

	elif direction == "L":

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Beginning of populating the place_holder[] in the global_variables.py 
		# using one row of the game board at a time going from top to bottom
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		while vertical_index < 4: # 4 here is the total # of columns in the game board.

			while horizontal_index < 4: # 4 here is the total # of rows in the game board.

				index = horizontal_index + (vertical_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.place_holder[horizontal_index] = global_variables.game_board[index]
				# horizontal_index here runs from 0 .... 3 and using it with global_variables.place_holder[] would save me setting up a for loop running from 0 to 3. The leftmost entry in a row of the game board maps into the leftmost entry of the place_holder[] in the global_variables.py.

				horizontal_index += 1	

			horizontal_index = 0 # This is done for the following while loop.

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# End of populating the place_holder[] in the global_variables.py using
		# one row of the game board at a time going from top to bottom
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			 
			move_and_add()
			# Add and move #'s inside the place_holder[] in the global_variables.py and move them to the low end of the array.

			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		
			# Copying the contents of the place_holder[] back into the appropriate
			# row, i.e. left to right of the place_holder[] would map into the
			# left to the right of the appropriate row of the game board.
			#
			# Note
			# ****
			# 
			# I only need one while loop as follows for while vertical_index < 4:
			# above can be reused.
			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
										
			while horizontal_index < 4: # 4 here is the total # of rows in the game board.

				index = horizontal_index + (vertical_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.game_board[index] = global_variables.place_holder[horizontal_index]
				# horizontal_index here runs from 0 .... 3 and using it with global_variables.place_holder[] would save me setting up a for loop running from 0 to 3.

				horizontal_index += 1	

			horizontal_index = 0
			
			vertical_index += 1

	elif direction == "R":

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# Beginning of populating the place_holder[] in the global_variables.py 
		# using one row of the game board at a time going from top to bottom
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		while vertical_index < 4: # 4 here is the total # of columns in the game board.

			while horizontal_index < 4: # 4 here is the total # of rows in the game board.

				index = horizontal_index + (vertical_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.place_holder[3 - horizontal_index] = global_variables.game_board[index]
				# horizontal_index here runs from 0 .... 3 and using it with global_variables.place_holder[] would save me setting up a for loop running from 0 to 3. The leftmost entry in a row of the game board maps into the rightmost entry of the place_holder[] in the global_variables.py.

				horizontal_index += 1	

			horizontal_index = 3 # This is done for the following while loop.

		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		# End of populating the place_holder[] in the global_variables.py using
		# one row of the game board at a time going from top to bottom
		# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			 
			move_and_add()
			# Add and move #'s inside the place_holder[] in the global_variables.py and move them to the low end of the array.

			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		
			# Copying the contents of the place_holder[] back into the appropriate
			# row, i.e. left to right of the place_holder[] would map into the
			# left to the right of the appropriate row of the game board.
			#
			# Note
			# ****
			# 
			# I only need one while loop as follows for while horizontal_index >= 0:
			# above can be reused.
			# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
										
			while horizontal_index >= 0: 

				index = horizontal_index + (vertical_index * 4) 
				# This is calculating indices to index into the columns of the game board. 

				global_variables.game_board[index] = global_variables.place_holder[3 - horizontal_index]
				# horizontal_index here runs from 0 .... 3 and using it with global_variables.place_holder[] would save me setting up a for loop running from 0 to 3.

				horizontal_index -= 1	

			horizontal_index = 0
			
			vertical_index += 1
