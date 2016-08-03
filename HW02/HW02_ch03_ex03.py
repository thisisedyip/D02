#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def do_twice(f, s):
	f(s)
	f(s)

def do_four(f, s):
	do_twice(f, s)
	do_twice(f, s)

def print_twice(s):
	print(' ', end=s)
	print(' ', end=s)

"""Constructing a line"""

def linestart(s): #start of line
	print(end=s)
	do_twice(print_twice, '-')
	print(end=' ')

def lineend(s): #end of line
	print(end=s)
	print()

""" Constucting the beams"""

def beamstart(s): #start of beam
	print(end=s)
	do_twice(print_twice, ' ')
	print(end=' ')

def beamend(s): #end of beam
	print(end=s)
	print()

def beamall2(s): #1 row of beams for 2x2
	do_twice(beamstart, s)
	beamend(s)

def beamall4(s): #1 row of beams for 4x4
	do_four(beamstart, s)
	beamend(s)


""" Constructing the 2x2 box """

def two_by_two():
	"""top line""" 
	do_twice(linestart, '+')
	lineend('+')

	"""beams 1"""
	do_four(beamall2, '|')

	"""middle line"""
	do_twice(linestart, '+')
	lineend('+')

	"""beams 2"""
	do_four(beamall2, '|')

	"""bottom line"""
	do_twice(linestart, '+')
	lineend('+')

def four_by_four():
	"""top line""" 
	do_four(linestart, '+')
	lineend('+')

	"""beams 1"""
	do_four(beamall4, '|')

	"""bottom line 1"""
	do_four(linestart, '+')
	lineend('+')

	"""beams 2"""
	do_four(beamall4, '|')

	"""bottom line 2"""
	do_four(linestart, '+')
	lineend('+')

	"""beams 3"""
	do_four(beamall4, '|')

	"""bottom line 3"""
	do_four(linestart, '+')
	lineend('+')

	"""beams 4"""
	do_four(beamall4, '|')

	"""bottom line 4"""
	do_four(linestart, '+')
	lineend('+')



# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    
    two_by_two()
    four_by_four()


if __name__ == "__main__":
    main()
