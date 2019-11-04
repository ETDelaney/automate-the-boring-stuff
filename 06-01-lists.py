# lists

# 1) you use brackets...


['cat', 'dog', 'elephant']

# 2) you can set the list to variable and then slice and dice...

spam = ['cat', 'dog', 'elephant']

spam[0]

# 3) you can have lists within lists and call them likewise...

spam = [['cat', 'dog', 'elephant'], [1,2,3]]

spam[1][0] # that would give you 1

# 4) you can also re-assign and can delete

del spam[1][0]

spam[1][1:] = [5,6,7]

# 5) there is also a list function to break something into a list

list('hello')

# which would return ['h', 'e', 'l', 'l', 'o']

# 6) can also concatenate and multiply etc.

[1,2,3] + [4,5,6] # gives [1, 2, 3, 4, 5, 6]

[1,2,3] * 3 # gives [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 7) finally you can use the 'in' and 'not in' to see if something is within a list

'howdy' in ['hello', 'howdy', 'hi']

42 not in ['hello', 'howdy', 'hi']

# both would evaluate to true
