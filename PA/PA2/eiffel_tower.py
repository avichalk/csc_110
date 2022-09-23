#Author: Avichal Kaul
#Description: prints out the eiffel tower
#Comments: give it to me straight doc- is this a jojo reference?

size = int(input('Enter Eiffel tower size:\n'))
uh = int(size*1.5)
mw = int((size*2)+1)
mh = int((size/2)+3)
lw = int((size*4)+1)
lh = (int(size/1.5))
lhmh = int((lw-mw)/2)
lhuh = int((lw-3)/2)

print('')

print('   ' + ' '*lhuh + ' $')
print(('   ' + ' '*lhuh + '|Z|\n')*uh, end='')
print('  ' + ' '*lhmh +'/' + 'Z'*mw +'\\')
print(('  ' + ' '*(lhmh) + 'H' + ' '*mw +'H\n')*mh, end='')
print('  /' + '%'*lw + '\\')
print((' ##' + ' '*lw + '##\n')*lh, end='')
print(('## ' + ' '*lw + ' ##\n')*lh, end='')