
# Simon Peter followed Jesus, as did another disciple. Now that disciple was known to the high priest, and entered in with Jesus into the court of the high priest (John 18:15)

# Ask Python to print sqrt(25) on line 3.
import math
print (math.sqrt(25))

"""
FUNCTIONS
Generic Imports
Did you see that? Python said: NameError: name 'sqrt' is not defined. Python doesn't know what square roots are—yet.

There is a Python module named math that includes a number of useful variables and functions, and sqrt() is one of those functions. In order to access math, all you need is the import keyword. When you simply import a module this way, it's called a generic import.
1.
You'll need to do two things here:

Type import math on line 2 in the editor.
Insert math. before sqrt() so that it has the form math.sqrt(). This tells Python not only to import math, but to get the sqrt() function from within math. Then hit Run to see what Python now knows.

"""

# but Peter was standing at the door outside. So the other disciple, who was known to the high priest, went out and spoke to her who kept the door, and brought in Peter. (John 18:16)

# Import *just* the sqrt function from math on line 3!

from math import sqrt


"""
FUNCTIONS
Function Imports
Nice work! Now Python knows how to take the square root of a number.

However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt().

It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword:

from module import function
Now you can just type sqrt() to get the square root of a number—no more math.sqrt()!
Instructions
1.
Let's import only the sqrt function from math this time. (You don't need the () after sqrt in the from math import sqrt bit.)
"""
