#Author: Avichal Kaul
#Description: Decrypts a file the encrypter encrypted for us
#Comments:

filename1=input('Enter the name of an encrypted text file:\n')
filename2=input('Enter the name of the encryption index file:\n')

file1=open(filename1, mode='r')
lines=file1.readlines() ## intializing more lists
lines=[i.strip('\n') for i in lines] ## removes /n from all elements
file2=open(filename2, mode='r')
index=file2.readlines() ## another list
index=[i.strip('\n') for i in index] ## removes /n from all elements
index=[int(i) for i in index] ## converts all values from string into integer
index=[i-1 for i in index] ##subtracts one because adding one was dumb nad pointless
storage=[]
lines2=[]
w=0
while w<len(index): ## creating the list for the decrypted file. All the values thus initialized will be overwritten
    lines2.append(w)
    w+=1
i=0
while i<len(index): ## swa
    lines2[int(index[i])]=lines[i]
    i+=1
lines2=[i+'\n' for i in lines2] ## adds /n to all elements
open('decrypted.txt',mode='w').writelines(lines2)