#Author: Avichal Kaul
#Description: gives you a cool avatar
#Comments: realised i hadn't put in the description and comments at 1am
## but i had to get out of bed, trudge over to my laptop, turn it on,
## and then put this in. it feels silly to just write one line and then
## go back to sleep, so here's a thing vaguely related to the pa
## Jane. Chris. custom. Jeff.
## Long ago, the four nations lived in lived together in harmony.
## then, everything changed when Chris spat out this really
## weird error that messed everything up for two days and
## then just kinda disappeared, not really sure what happened
## alright im done bye

print('----- AVATAR -----')
avatar = input('Select an Avatar or create your own:\n')
while avatar != 'Chris' and avatar != 'Jane' and avatar != 'Jeff' and avatar != 'custom' and avatar == '':
    avatar = input('Select an Avatar or create your own:\n')

##avatar = 'Jeff'
##n = 0

## NOT ALLOWED GLOBAL VARIABLES. YEET ALL THIS
## ALSO NO STRING MULTIPLICATION, OH FRICK OH HECK
##WHY DIDN'T I READ THE FULL DOCUMENTATION
#h = 'front' ##hat
#e = 'u' ##eyes
#long_hair = False
#a = 'f' ##arms
#t = 5 ##torso
#l=1 ##legs
#s= 'bbbbb' ##shoes, make it five characters

## hat
def hat(h):
    print('       ~-~     ')
    print('     /-~-~-\   ')
    if h == 'right':
        print('    /_______\___')
    elif h == 'left':
        print(' ___/_______\    ')
    elif h == 'both':
        print(' ___/_______\___ ')
    else:
        print('    /_______\\')

## face
def face(long_hair,e):
    if long_hair == 'False':
        print("    |'''''''|")
        print('    | ' + e + '   ' + e + ' |    ')
        print('    |   V   |     ')
        print('    |  ~~~  |     ')
        print('     \_____/ ')
    elif long_hair == 'True':
        print('   "|"""""""|"')
        print('   "| ' + e + '   ' + e + ' |"   ')
        print('   "|   V   |"    ')
        print('   "|  ~~~  |"    ')
        print('   " \_____/ "')

## arms
def arms(n,a):
    if n == 1:
        print('      |-X-|')
    print(' 0' + a+a+a+a + '|---|' + a+a+a+a + '0')

## torso
def torso(t):
    i=0
    while i<t:
        print('      |-X-|')
        t=t-1
    print('      HHHHH ')

## legs
def legs(l):
    i=0
    j=1
    k=4
    while i < l:
        print(' '+' '*(k) + '///' + ' '*(j) + '\\\\\\')
        i=i+1
        j=j+2
        k=k-1
        ##??? weirdest bug ever

## shoes
def shoes(s):
    print(s+'       '+s)

#main
def main():
    if avatar != 'custom':
        if avatar == 'Jeff':
            print('')
            hat('both')
            face('False','0')
            arms(1,'=')
            torso(4)
            legs(2)
            shoes('#HHH#')
        elif avatar == 'Chris':
            print('')
            hat('front')
            face('False','U')
            arms(1,'W')
            torso(2)
            legs(4)
            shoes('<>-<>')
            ## big ol bug with chris, why?
        elif avatar == 'Jane':
            print('')
            hat('right')
            face('True','*')
            arms(0,'T')
            torso(2)
            legs(3)
            shoes('<|||>')
    elif avatar == 'custom':
        print('Answer the following questions to create a custom avatar')
        h = input('Hat style ?\n')
        e = input('Character for eyes ?\n')
        long_hair = input('Long hair (True/False) ?\n')
        a = input('Arm style ?\n')
        t = int(input('Torso length ?\n'))
        l = int(input('Leg length (1-4) ?\n'))
        s = input('Shoe look ?\n')
        print('')
        hat(h)
        face(long_hair,e)
        arms(0,a)
        torso(t)
        legs(l)
        shoes(s)

main()