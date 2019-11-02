# sum numbers

total = 0
max_number = 0
print('What number from 0 to n do you want to sum up to?')

while True:
    max_number = input()

    # this is known as input validation
    try:
        if int(max_number) > 0:
            break
        
    except:
        print("sorry, please re-enter an integer value")
        continue

    print("sorry, please re-enter an integer value that is positive")
    

max_number = int(max_number)

for i in range(max_number+1): # python is exlusive of last number
    total += i

print('The sum is: ' + str(total))
    
