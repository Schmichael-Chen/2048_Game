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

# 1) http://www.ibm.com/developerworks/library/os-python8/

# 2) http://stackoverflow.com/questions/12330522/reading-a-file-without-newlines

# 3) http://stackoverflow.com/questions/82831/how-do-i-check-if-a-file-exists-using-python

# 4) http://stackoverflow.com/questions/9381463/how-to-create-a-file-in-linux-from-terminal-window

# 5) http://stackoverflow.com/questions/17115664/can-linux-cat-command-be-used-for-writing-text-to-file

import os 

import os.path

from sys import stdout

import global_variables

from __print__ import __print__ 

def best_score():

	if os.path.isfile("score_file.txt") == False:

		os.system("echo 0 > score_file.txt")	

		stdout.write("\nBest Score: ")

		__print__(0)

	else:

		score_from_score_file = open("score_file.txt",'r').read().split('\n')

		stdout.write("\nBest Score: ")

		if score_from_score_file[0] > global_variables.score:

			__print__(score_from_score_file[0])

		else:

			__print__(global_variables.score)
