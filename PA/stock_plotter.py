#Author: Avichal Kaul
#Description: stocks some plots
#Comments: that test was way too long. and now there's this too?
##all the inputs
horiplot = '' #3change to 0 after testing
while horiplot != 'vertical' and horiplot != 'horizontal':
    horiplot = str(input('Enter stock plotter mode:\n'))
string = str(input('Enter stock plot input string:\n'))
while int(len(string)) % 2 != 0:
    string = str(input('Enter stock plot input string:\n'))
##string = 'u2u2u2u2d2d2d2d2d2d2d2d2u2u2u2u2u2u2u2u2' ##change to 0 after testing
i=0
y=17
z = len(string)//2+2




##vertical plot stuff (and horizontal plot stuff too)
if horiplot == 'vertical':
    x=8
    print('#'*19)
    while int(i) < len(string):
        if string[i] == 'u':
            x = x + int(string[i+1])
            print('#' + ' '*x + '*' + ' '*(16-x) + '#')
            i = i+2
        elif string[i] == 'd':
            x = x - int(string[i+1])
            print('#' + ' '*x + '*' + ' '*(16-x) + '#')
            i=i+2
    print('#'*19)
elif horiplot == 'horizontal':
    i=0
    x=9
    print('#'*(int(z)+2))
    while y > 0:
        print('# ', end='')
        for i in range(0,len(string)):
            c = ''
            if string[i] == 'u':
                x = x+int(string[i+1])
                if x == y:
                    c = c+'*'
                elif x != y:
                    c = c + ' '
            elif string[i] == 'd':
                x = x-int(string[i+1])
                if x == y:
                    c = c + '*'
                elif x != y:
                    c = c + ' '
            i = i+2
            print(c, end='')
        print(' #')
        x=9
        y = y-1
    print('#'*(int(z)+2))