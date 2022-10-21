num = int(input('Entre a year: '))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print(f'{num} is leap year')
        else:
            print(f'{num} is not leap year')
    else:
        print(f'{num}is leap year')
else:
    print(f'{num} is not leap year')