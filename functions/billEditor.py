
#  If the world hates you, you know that it has hated me before it hated you. (John 15:18)


def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)



"""
FUNCTIONS
What Good are Functions?
You might have considered the situation where you would like to reuse a piece of code, just with a few different values. Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.
1.
Check out the code in the editor. If you completed the Tip Calculator lesson, you'll remember going through and calculating tax and tip in one chunk of program. Here you can see we've defined two functions: tax to calculate the tax on a bill, and tip to compute the tip.

See how much of the code you understand at first glance (we'll explain it all soon). When you're ready, click Run to continue.


"""
