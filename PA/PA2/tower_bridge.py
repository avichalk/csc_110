#Author: Avichal Kaul
#Description: prints out the tower bridge
#Comments: everything about this code hurts from the hundreds and hundreds of u^W^us to 'tower height length'

length = int(input('enter bridge length:\n'))
lth = int(input('lower tower height length:\n'))
uth = int(input('upper tower height length:\n'))
width = int(input('enter tower width:\n'))

print('    +' + '  ' + ' '*width + '  +  ' + ' '*length + '  +  ' + ' '*width + '  +')
print(('    ' + '|||' + '^'*width + 'uu|  ' + ' '*length + '  |uu' + '^'*width + '|||\n')*uth, end='')
print('     \\u' + '^'*width +'u/===' + '='*length + '===\\u' + '^'*width +'u/')
print(('     |u' + '.'*width + 'u|   ' + ' '*length + '   |u' + '.'*width + 'u|\n')*lth, end='')
print('_____|u' + '.'*width + 'u|___' + '_'*length + '___|u' + '.'*width + 'u|_____')
print('====HHH' + 'H'*width + 'HH===' + '='*length + '===HH' + 'H'*width + 'HHH====')
print('    HHH' + 'H'*width + 'HH   ' + ' '*length + '   HH' + 'H'*width + 'HHH    ')
print('    HHH' + 'H'*width + 'HH   ' + ' '*length + '   HH' + 'H'*width + 'HHH    ')
print('    HHH' + 'H'*width + 'HH   ' + ' '*length + '   HH' + 'H'*width + 'HHH    ')
