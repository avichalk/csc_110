thing = input('Enter bar string:\n')
print('+---------+')
for i in range(0, len(thing)):
    print('|' + ' '*(9-int(thing[i])) + '#'*int(thing[i]) + '|')
print('+---------+')