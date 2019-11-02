# playing with python built-in functions...

# 1) python already comes with plenty of modules we can import...

#   such as random, os, sys, math, etc...

# 2) you can import all of them at once by doing...
#   import random, os, sys, math

#   or one-by-one via:
#   import random
#   import os
#   etc.

#   from there, you can call on the functions in those modules...
#   random.randint(1,10)

# 3) it is probably better to that, than:
#   from random import *

#   which allows you not to have to type out the module, but it makes
#   code less readable and could cause issues of overwriting other functions

#   ... now you could do:
#   randint(1,10)

# 4) to exist a program early... use:
#   sys.exit()

# 5) there are also third-party modules... numpy, etc.
# we will be trying pyperclip later on...


import sys
print('Hello')
sys.exit()
print('Good-bye') # notice this will never print
