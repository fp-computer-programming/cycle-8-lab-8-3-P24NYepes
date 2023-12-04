"""
Create a Python file named lab_8-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-3.py
Write the while-loop version of the following for-loop program.

def sum_to(n):
  total = 0
	for i in range(n+1):
		total += i
	return total

The function should be able to have an integer passed to it and return the sum of all the values from 1 to that integer
"""
# Nicholas Yepes 12/04/23

def sum_to(n):
  total = 0  #creates the variable 
  x = 1  #loop counter

    # begins the while loop counter
  while x <= n:
      total += x  # adds the variable i to the total
      x += 1  

  return total  # returns the total


result = sum_to(8)
print(result)  






