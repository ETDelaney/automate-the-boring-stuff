def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

# note that function that have no return statement, return a None value    

print(div42by(12))
print(div42by(2))
print(div42by(0))
print(div42by(21))
