# for loops, lists, etc.

# 1) for loops iterate over values in list
# 2) for the range() function to return list-like values, pass it to the
# ... the list() function


# use list(range(4)) to get [0,1,2,3]

supplies = ['pens', 'staplers', 'pencils', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
