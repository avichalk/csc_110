shape = input('Enter shape to display:\n')
while shape != 'hourglass' and shape != 'plumbbob' and shape != 'house':
    shape = input('Enter shape to display:\n')
a = input('Enter arrow character:\n')
h = int(input('Enter row-area height:\n'))

def up_arrow():
    ## as far as i can tell the
    ## height doesn't change
    print('     ' + a)
    print('    ' + a*3)
    print('   ' + a*5)
    print('  ' + a*7)
    print(' ' + a*9)
    print(a*11)

def down_arrow():
    ## just invert the up arrow
    print(a*11)
    print(' ' + a*9)
    print('  ' + a*7)
    print('   ' + a*5)
    print('    ' + a*3)
    print('     ' + a)

def middle_bit():
    ## yes it's not always in the
    ## middle, i know
    i=0
    while i<h:
        print('|---------|')
        i=i+1

def main():
    if shape == 'hourglass':
        print('')
        middle_bit()
        down_arrow()
        up_arrow()
        middle_bit()
        return
    elif shape == 'plumbbob':
        print('')
        up_arrow()
        middle_bit()
        down_arrow()
        return
    elif shape == 'house':
        print('')
        up_arrow()
        middle_bit()
        return

main()