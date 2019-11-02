print('How many cats do you have?')

while True:
    numCats = input()
    try:
        if int(numCats) < 0:
            print('non-negative integers please...')
            continue
        
        elif int(numCats) >= 4:
            print('Lots of cats!')
            break

        else:
            print('Manageable amount of cats.')
            break

    except:
        print('I need an integer of cats... preferably non-negative also.')
