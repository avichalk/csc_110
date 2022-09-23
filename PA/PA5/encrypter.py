#Author: Avichal Kaul
#Description: encrypts an input file and spits out an index too
#Comments:

import random ## imports random


filename=input('Enter a name of a text file to encrypt:\n')
random.seed(125)
file=open(filename, mode='r')
lines=file.readlines()
lines=[i.strip('\n') for i in lines] ## removes /n from all elements
lines=[i+'\n' for i in lines] ## adds /n to all elements
index=[] ## housekeeping, initializing several lists for storage and formatting them
w=0
while w<len(lines): ## creating our index file so it can be swapped around
    index.append(w)
    w+=1
storage=[]
randomno1=[] ## this to avoid repetition of indc
randomno2=[]
lenlines=5*len(lines)
i=0
while i<lenlines:
    rint1=random.randint(0,int(len(lines)-1))
    rint2=random.randint(0,int(len(lines)-1))
    randomno1.append(rint1)
    randomno2.append(rint2)
    storage.append(lines[rint1])
    lines[rint1]=lines[rint2]
    lines[rint2]=storage[0]
    index[rint2], index[rint1] = index[rint1], index[rint2]
    storage.clear()
    i+=1
index=[i+1 for i in index] ##adds 1 to each element because for some inconcievable reason we have to do that
index=[str(i)+'\n' for i in index] ## adds \n no all elements

open('index.txt', mode='w+').writelines(index)
file.close()
open('encrypted.txt',mode='w+').writelines(lines)

