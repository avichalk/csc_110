thing = input('Enter bar string:\n')
print('+---------+')
for i in range(0, len(thing)):
    print('|' + '#'*int(thing[i]) + ' '*(9-int(thing[i])) + '|')
print('+---------+')