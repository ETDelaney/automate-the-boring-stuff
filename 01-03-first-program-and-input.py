# This program says hello and ask for your name

# notice how we call the print() and input() functions
# functions can be thought of as mini-programs inside a program

print('Hello world!') # we call the print function and pass an argument

print('What is your name?')
myName = input() # input function waits for input
print('It is nice to meet you, ' + myName)

print('As a machine, my only relationship to your name is its length - which is: ')
print(str(len(myName)) + ' characters long.')

print('Please input your age: ')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
