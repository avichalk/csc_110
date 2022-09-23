#Author: Avichal Kaul
#Description: processes a CSV file,
## gets user input- filename, column and operation,
## and using them goes through the csv file to
## get minimums, averages, and maximums for several
## different columns
#Comments:

def main():
    '''
    main function, accepts user inputs and
    processes them to pass into three functions
    for subsequent processing. It does not return anything
    '''
    filename=input('Enter CSV file name:\n')
    column=int(input('Enter column number:\n'))
    operation=input('Enter column operation:\n')
    file=open(filename, mode='r')
    lines_list=file.readlines()
    values_2d=[] #initializing list of lines and 2d list
    for i in lines_list:
        i=i.strip('\n')
        values_2d.append(i.split(','))
    if operation=='min':
        minimum(values_2d, column)
    elif operation=='avg':
        avg(values_2d, column)
    elif operation=='max':
        maximum(values_2d, column)

def minimum(values_2d, column):
    '''
    gets the minimum value of the user selected
    column. it does not return anything, but directly
    prints
    '''
    column=column-1 ## making column work with list
    total=0
    minimum=values_2d[0][column]
    i=0
    while i<len(values_2d):
        total+=float(values_2d[i][column])
        if values_2d[i][column]<minimum:
            minimum=values_2d[i][column]
        i+=1
    avg=total/len(values_2d)
    print('The minimum value in column', column+1, 'is:', minimum)

def avg(values_2d, column):
    '''
    gets the average value of the user selected
    column. it does not return anything, but directly
    prints
    '''
    total=0
    column=column-1
    maximum=values_2d[0][column]
    i=0
    while i<len(values_2d):
        total+=float(values_2d[i][column])
        i+=1
    avg=float(total/len(values_2d))
    print('The average for column', column+1, 'is:', avg)


def maximum(values_2d, column):
    '''
    gets the maximum value of the user selected
    column. it does not return anything, but directly
    prints
    '''
    total=0
    column=column-1
    maximum=values_2d[0][column]
    i=0
    while i<len(values_2d):
        total+=float(values_2d[i][column])
        if values_2d[i][column]>maximum:
            maximum=values_2d[i][column]
        i+=1
    avg=total/len(values_2d)
    print('The maximum value in column', column+1, 'is:', maximum)

main()