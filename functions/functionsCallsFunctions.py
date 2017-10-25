
# I have told you these things, that in me you may have peace. In the world you have oppression; but cheer up! I have overcome the world. (John 16:33)



def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2





"""
FUNCTIONS
Functions Calling Functions
We've seen functions that can print text or do simple arithmetic, but functions can be much more powerful than that. For example, a function can call another function:

def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) + 7
Instructions
1.
Let's look at the two functions in the editor: one_good_turn (which adds 1 to the number it takes in as an argument) and deserves_another (which adds 2).

Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.


def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return n + 2
"""
