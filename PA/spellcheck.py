#Author: Avichal Kaul
#Description: does a thing where it checks
## spellings using a dictionary you have to give it
#Comments: It's 3:30AM on a saturday night, I haven't enjoyed
## halloween one bit, which is my favourite holiday by the way,
## my favourite holiday which this year had a full moon,
## we had a full moon on halloween, a FULL MOON
## there might never be another full moon
## halloween for the rest of my life far as i know
## but hey, gotta get that education amirite
## anyways this is basically working but
## i'm not going to turn it in until tomorrow because
## if something goes wrong I'm afraid I'll go properly feral
## smash my computer to bits, rip my clothes off, bite stuff,
## mess around and yeet myself into the godforsaken wilderness
## to become one with the coyotes and the other college dropouts
## or perhaps succumb to the harsh winter and be reduced to a
## particularly bitter bit of carrion
## 'tastes funny', the scavengers might comment as they munch on my
## rotting extremities. 'tastes of bitterness and regret'

def main(): ##main
    read_misspellings()
    fileinput=str(input('Enter input file:\n'))
    ##fileinput='testfile.txt'
    file=open(fileinput, mode='r')
    mode=str(input('Enter spellcheck mode (replace or suggest):\n'))
    ##mode='suggest'
    filelines=file.readlines()
    ##print(filelines)
    global filewords
    filewords=[i.split(' ') for i in filelines] ## this creates lists within a list
    if mode=='replace':                         ## (but that's alright)
        replace_mode()
    elif mode=='suggest':
        suggest_mode()
    ## mostly housekeeping, all user inputs and
    ## initializing our most important lists
    ## and getting modes working

def read_misspellings():
    global misdict
    misdict={} ##defining misspellings dictionary
    mis=open('misspellings.txt', mode='r')
    lines=mis.readlines()
    lines=[i.strip('\n') for i in lines] ## opening file and removing \n
    ##print(lines)
    for i in lines:
        i=i.split(':') ## seperating correct and incorrect spellings
        ##print(i)
        j=i[1].split(',') ## seperating different incorrect spellings
        ##print(j)
        for k in j: ## using for loop to put the incorrect spellings into our dictionary
            misdict[k]=i[0]
    ##print(misdict)

def replace_mode():
    global printlist
    printlist=[] ## to better format the output
    n=''
    m=''
    wasupper=''
    for i in filewords:
        ##print(i)
        for j in i:
            ##print(j[-2:])
            if j=='\n':
                printlist.append(j) ## the possibility for a completely
                break               ## blank line was never mentioned in
                ## the documentation, which is why it caused a big ol'
                ## runtime error. It took twenty minutes of copying and
                ## pasting the test cases from gradescope and removing the
                ## spaces and stuff for me to realise the program crashed
                ## at i=\n. I'm begging you guys, please give us the option
                ## to download the test cases from gradexcope, or at least
                ## mention stuff like this. I don't know. Please. We're tired.
            if j[0].isupper()==True: ## capitalization hijinks
                wasupper=1
                j=j.lower()
            else:
                wasupper=0
            if '\n' in j: ## preserve formatting
                n='\n'
                j=j[0:-1]
                ##print(j)
            else:
                n=''
            if j[-1]==',' or j[-1]=='.' or j[-1]=='?' or j[-1]=='!':
                ## preserve punctuation
                m=j[-1]
                j=j[0:-1]
            else:
                m=''
            if j in misdict: ##spellcheck
                ##print(j)
                j=misdict[j]
            if wasupper==1: ## was it upper check
                j=j.capitalize()
            printlist.append(j+m+n)
    finalformat='' ## string to store the final output
    for i in printlist: ##output specific to replace_mode
        if '\n' in i: ## to remove extra space after endline
            finalformat+=i
        else:
            finalformat+=i+' '
    print('\n--- OUTPUT ---')
    print(finalformat)

def suggest_mode():
    printlist=[]
    n=''
    m=''
    count=0
    wasupper=''
    listofshame=[] ## list of misspelled words
    for i in filewords:
        ##print(i)
        for j in i:
            if j=='\n': ## blank like preservation
                printlist.append(j)
                break
            ##print(j[-2:])
            if j[0].isupper()==True: ## capitalization hijinks
                wasupper=1
                j=j.lower()
            else:
                wasupper=0
            if '\n' in j: ## preserve formatting
                n='\n'
                j=j[0:-1]
                ##print(j)
            else:
                n=''
            if j[-1]==',' or j[-1]=='.' or j[-1]=='?' or j[-1]=='!':
                ## preserve punctuation
                m=j[-1]
                j=j[0:-1]
            else:
                m=''
            if j in misdict: ##spellcheck
                count+=1
                h=misdict[j]
                if wasupper==1: ## bit further down does same thing but hey it works
                    h=h.capitalize()
                listofshame.append(str('('+str(count)+') '+h)) ## for legend
                k=' ('+str(count)+')'
                m+=k ## for rest of the output. this bit was really unintuitive
            if wasupper==1: ## was it upper check
                j=j.capitalize()
            printlist.append(j+m+n)
    finalformat=''
    for i in printlist: ##output specific to suggest_mode
        if '\n' in i: ## even i don't know what this does
            finalformat+=i ## figured it out, it removes the
        else:               ## extra space after the endline
            finalformat+=i+' '
    print('\n--- OUTPUT ---')
    print(finalformat)
    print('--- LEGEND ---')
    for i in listofshame:
        print(i)

main() ## main