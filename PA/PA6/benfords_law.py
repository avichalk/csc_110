#Author: Avichal Kaul
#Description: This is a program that processes a CSV file given by
## the user, and uses it to create a graph of the first character of
## each number used in the file. It uses this graphical aid to illustrate
## effectively whether or not the numbers in the file follow Benford's Law
#Comments:

def main():
    '''
    This is our main function. It accepts an input from the user that is
    the name of a file, and processes it such that only numbers that don't
    start with a 0 are put into the 'numbers' list. it then passes this list
    into graphics_output
    '''
    filename=input('Data file name:\n')
    file=open(filename, 'r')
    lines=file.readlines()
    numbers=[]
    for i in lines:
        i=i.split(',')
        for j in i:
            j=j.strip('\n')
            if j[0]!='0' and j[0].isdigit() and j[-1].isdigit():
                numbers.append(float(j))
    ## processes the data to ensure no unwanted numbers make it into
    ## our list
    graphics_output(numbers)

def graphics_output(numbers):
    '''
    This function is named so because it outputs the "bar graph" used to
    illustrate Benford's Law. In essence, it processes the data in the
    'numbers' list and passes it through into a dictionary number_dic,
    which it can use to keep track of the numbers. It processes the percentage
    of list entries beginning with a certain number into a list, and uses it to
    print the graph. It also passes said list into another function, benfords_law,
    which determines whether or not the data follows Benford's Law
    '''
    numbers_but_strings=[]
    for i in numbers:
        numbers_but_strings.append(str(i)) ## making all the numbers strings again
    number_dic={}
    for i in numbers_but_strings:
        number_dic[i[0]]=0
    for i in numbers_but_strings:
        number_dic[i[0]]+=1 ## initializing and counting the number of numbers
    percent=[]
    i=1
    while i<10:
        percent.append(int((number_dic[str(i)]/len(numbers_but_strings))*100))
        i+=1 ## getting the percentage of numbers that begin with a certain number
    i=0
    print()
    while i<9: ## printing the bar graph
        print(i+1, '|', '#'*round(percent[i]))
        i+=1
    check = benfords_law(percent)
    if check==9: ## checking if the data follows Benford's Law
        print("\nFollows Benford's Law")
    else:
        print("\nDoes not follow Benford's Law")

def benfords_law(percent):
    '''
    Accepts a list of percentages and, with some hardcoded
    instructions, determines whether or not the data follows
    Benford's Law. It returns check to graphics_output,
    which will be 9 if Benford's Law is followed
    '''
    i=0
    check=0
    while i<9:
        if i==0:
            if percent[i]<40 and percent[i]>25:
                check+=1
        if i==1:
            if percent[i]<27 and percent[i]>12:
                check+=1
        if i==2:
            if percent[i]<22 and percent[i]>7:
                check+=1
        if i==3:
            if percent[i]<19 and percent[i]>4:
                check+=1
        if i==4:
            if percent[i]<17 and percent[i]>2:
                check+=1
        if i==5:
            if percent[i]<16 and percent[i]>1:
                check+=1
        if i==6 or i==7:
            if percent[i]<15 and percent[i]>0:
                check+=1
        if i==8:
            if percent[i]<14 and percent[i]>0:
                check+=1
        i+=1
    return check

main()