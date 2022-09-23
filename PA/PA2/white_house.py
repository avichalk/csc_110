#Author: Avichal Kaul
#Description: prints out a model of the white house
#Comments: how do you remove a trailing newline i forgot (nvm i remembered)

swidth = int(input('Specify side width:\n'))
mwidth =  int(input('Specify middle width:\n'))
fheight = int(input('Specify flag height:\n'))
height = int(((swidth+mwidth)/4)+1)

print('')
print(' '+'   '*swidth+'    '*mwidth+'|##')
print((' '+'   '*swidth+'    '*mwidth+'|\n')*fheight, end='')
print(" "+"   "*swidth+".-.-"*mwidth+"''"+"-.-."*mwidth)
print(' '+'   '*swidth+';.__'*mwidth+'--'+'__.;'*mwidth)
print('.' + '___'*swidth + '[---'*mwidth +'--'+'---]'*mwidth+'___'*swidth+'.')
print(('|' + 'II '*swidth + '||II'*mwidth + 'HH' +'II||'*mwidth + ' II'*swidth + '| \n|' + '.. '*swidth + '||..'*mwidth +'||' + '..||'*mwidth + ' ..'*swidth + '|\n')*height)