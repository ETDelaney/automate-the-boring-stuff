# a summary on functions and the print statement

# 1) functions are there to get rid of duplicate code

# 2) input to functions are arguments

# 3) the parameters are the variables in the function's parentheses

# 4) function return value is specified via return

# 5) every function has a return value... if no return, default is None

# 6) there are keyword arguments that are optional...

# 7) for example, print() function has the keyword arguments 'end' and 'sep'

print('Hello')
print('World')

# notice that after print it defaults to end = '\n'

# you could change this to:
print('Hello', end='')
print('world')

# could also do....
print('cat', 'mouse', 'dog')

# or change the seperation to ABC:
print('cat','mouse', 'dog', sep = 'ABC')
