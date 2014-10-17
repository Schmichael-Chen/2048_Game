#!/usr/bin/python

'''

Copyright (c) 2014 Schmichael Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: Schmichael Chen <schchen2000@yahoo.com>

'''

import global_variables

def move():

	index_1 = 0 # Index for 0's

	index_2 = 1 # Index for non-zeros

	temp_value = 0

	while index_1 < 3:

        	while index_2 < 4:

                	if global_variables.place_holder[index_1] == 0 and global_variables.place_holder[index_2] == 0:

                        	index_2 += 1

			elif global_variables.place_holder[index_1] == 0 and global_variables.place_holder[index_2] > 0:

				temp_value = global_variables.place_holder[index_1]

                	        global_variables.place_holder[index_1] = global_variables.place_holder[index_2]

                        	global_variables.place_holder[index_2] = temp_value

	                        index_1 += 1

        	                index_2 += 1

			elif global_variables.place_holder[index_1] > 0 and global_variables.place_holder[index_2] == 0:

				index_1 = index_2

	                        index_2 += 1

			elif global_variables.place_holder[index_1] > 0 and global_variables.place_holder[index_2] > 0:

                	                index_1 = index_2

                        	        index_2 += 1

		if index_2 == 4:

			break
