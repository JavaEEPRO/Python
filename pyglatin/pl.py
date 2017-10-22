

#  I command these things to you, that you may love one another. (John 15:17)


pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'empty'
  
  """
  PYGLATIN
Testing, Testing, is This Thing On?
Yay! You should have a fully functioning Pig Latin translator. Test your code thorougly to be sure everything is working smoothly.

You'll also want to take out any print statements you were using to help debug intermediate steps of your code. Now might be a good time to add some comments too! Making sure your code is clean, commented, and fully functional is just as important as writing it in the first place.
Instructions
1.
When you're sure your translator is working just the way you want it, click Run Code to finish this project.
  
  """
