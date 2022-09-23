thing = input('Enter bar string:\n')
print('+------------------+')
i=0
while i < int(len(thing)-1):
    print('|' + ' '*(9-int(thing[i])) + '#'*int(thing[i]) + '#'*int(thing[i+1]) + ' '*(9-int(thing[i+1])) + '|')
    i = i+2
print('+------------------+')