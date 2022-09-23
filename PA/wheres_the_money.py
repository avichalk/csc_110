#Author: Avichal Kaul
#Description: provides help with all your money laundering needs
#Comments: I was about to make an arrested development joke here, but the one I wanted to go with
#          doesn't really work in an academic setting. So here's CONMAN 2 instead.

import sys
print('-----------------------------')
print("----- WHERE'S THE MONEY -----")
print('-----------------------------')

salary = input('What is your annual salary?\n')
if salary.isnumeric() is False:
    print('Must enter positive integer for salary.')
    sys.exit()
else:
    salary = int(salary)
rent = input('How much is your monthly mortgage or rent?\n')
if rent.isnumeric() is False:
    print('Must enter positive integer for mortgage or rent.')
    sys.exit()
else:
    rent = int(rent)
bills = input('What do you spend on bills monthly?\n')
if bills.isnumeric() is False:
    print('Must enter positive integer for bills.')
    sys.exit()
else:
    bills = int(bills)
grocery = input('What are your weekly grocery/food expenses?\n')
if grocery.isnumeric() is False:
    print('Must enter positive integer for food.')
    sys.exit()
else:
    grocery = int(grocery)
travel = input('How much do you spend on travel annually?\n')
if travel.isnumeric() is False:
    print('Must enter positive integer for travel.')
    sys.exit()
else:
    travel = int(travel)
#test case
#salary = int(40000)
#rent = int(2000)
#bills = int(300)
#grocery = int(150)
#travel = int(4000)

#turns out code works just fine without these. don't know why it wasn't working before. pixies in the system bus?
tax = 0
#anrent = 0
#anbills = 0
#angrocery = 0

#tax stuff
if salary <= 15000 and salary >= 0:
    tax = salary*0.10
elif salary <=75000 and salary >= 15000:
    tax = salary*0.20
elif salary <=200000 and salary >= 75000:
    tax = salary*0.25
elif salary >=200000:
    tax = salary*0.30

#print(tax) #remove at end

#rent and bills and stuff
anrent = rent*12
anbills = bills*12
angrocery = grocery*52

#print(anrent, anbills, angrocery) #remove at end

# i forgot about the extra
extra = float(salary-anrent-anbills-angrocery-travel-tax)

#percentage!!!
prent = str(format(float(anrent/salary*100), '5,.1f' ))
pbills = str(format(float(anbills/salary*100), '5,.1f'))
pgrocery = str(format(float(angrocery/salary*100), '5,.1f'))
ptravel = str(format(float(travel/salary*100), '5,.1f'))
ptax = str(format(float(tax/salary*100), '5,.1f'))
pextra = str(format(float(extra/salary*100), '5,.1f'))

##'s!
hashrent = round(int(float(prent)), 2)
hashbills = round(int(float(pbills)), 2)
hashg = round(int(float(pgrocery)), 2)
hashtravel = round(int(float(ptravel)), 2)
hashtax = round(int(float(ptax)), 2)
hashextra = round(int(float(pextra)), 2)

#ohgodtheformatting
rentstr = str(format(anrent, '11,.2f'))
billstr = str(format(anbills, '11,.2f'))
grostr = str(format(angrocery, '11,.2f'))
trastr = str(format(travel, '11,.2f'))
taxstr = str(format(tax, '11,.2f'))
exstr = str(format(extra, '11,.2f'))

#print(rentstr, billstr, grostr, trastr)

#making ol' mate table look all dapper
thing = max(hashrent, hashbills, hashg, hashtravel, hashtax, hashextra)

#if extra <= 0:
 #   hashextra = 0
#also didn't need this`


#ol' mate table
print('')
print('-'*42 + '-'*thing)
print('See the financial breakdown below, based on a salary of $' + str(salary))
print('-'*42 + '-'*thing)
print('| mortgage/rent | $' + rentstr + ' | ' + prent + '% | ' + '#'*hashrent)
print('|         bills | $' + billstr + ' | ' + pbills + '% | ' + '#'*hashbills)
print('|          food | $' + grostr + ' | ' + pgrocery + '% | ' + '#'*hashg)
print('|        travel | $' + trastr + ' | ' + ptravel + '% | ' + '#'*hashtravel)
print('|           tax | $' + taxstr + ' | ' + ptax +'% | ' + '#'*hashtax)
print('|         extra | $' + exstr + ' | ' + pextra + '% | ' + '#'*hashextra)
print('-'*42 + '-'*thing)

if extra <= 0:
    print('>>> WARNING: DEFICIT <<<')
if tax >= 75000:
    print('>>> TAX LIMIT REACHED <<<')
