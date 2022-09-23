#Author: Avichal Kaul

#Description: This program takes a string input from the user that is assumed
## to be the name of a text file. the file is assumed to contain only lines
## of plain text that we must process. the lines and words in the file will
## be looped through to find various statistics , that will then be displayed
## as plain text and bar graphs in a gui. this program outputs nothing but that
## gui, but it gets there via approx 300 lines of code.

#Comments: Didn't realise we had to write a thesis for every single program.
## At least I know what I was losing all those marks now, thank you Instructor Aliyah.

def main():
    '''
    this is our main function, it accepts a string input
    from the user presumed to contain the name of the file
    it then opens the file, and passes this into a function
    file_read. it goes through all the other functions in the
    program as well, save one.
    '''
    name = input('Please enter the file name:\n')
    file=open(name, mode='r') ## opens file

    ## begin functions

    words_dic=file_read(file) ## reads file and returns a dictionary

    capital, punctuation, is_punctuated, isnt_punctuated, \
        words_dic, greatest_used, storage = file_sort(words_dic)
    ## passes file through to file_sort function, which returns various
    ## lists and dictionaries into which the words have been sorted.

    percentage, greatest_used, storage, word_list \
        =word_len_function(capital, punctuation, is_punctuated, isnt_punctuated, \
        words_dic, greatest_used, storage)
    ## the word_len_function exceeded the 30 line limit, so it works in tandem with
    ## storage_for_formatting, from which it returns a list of percentages, some stats,
    ## and the full unique word list.

    graphics_stuff(percentage, name, greatest_used, storage, word_list)
    ## graphics_stuff uses all these lists to create a gu interface
    ## which it can display all the values on. it takes in the parameters
    ## retrned by the previous functions, and does not return anything.

def file_read(file):
    '''
    this function uses one parameter- a string that contains the
    filename- reads all the lines in the file and puts
    them in a list. it removes \n from that list, or at least
    tries to (it's not very good at it). it then creates a second
    list, and puts the lines into that. unless of course the line
    has a lot of unnessecary spaces, in which case it just doesn't
    work. it puts those words into a list then puts that list into
    a dictionary, then adds the amount of times that word has occured.
    the dictionary it returns is fed into file_sort
    '''
    lines=file.readlines() ## reads lines

    words=[] ## creating the word list
    words_dic={} ## creating the dictionary
    for i in lines:
        i=i.strip() #3 removing \n attempt 2. this one works.
        i=i.split(' ')## splits line into a list of words. this is why
        for j in i:     ## several spaces confuse it. uses individual words
            if j!='':
                words.append(j) ## and adds them to this list
    for i in words: ## get the dictionary intialized with all our words
        words_dic[i]=0
    for i in words: ## populates the dictionary with the number of each word
        words_dic[i]+=1 ## yes, this is inefficient and loops
    return words_dic ## through the entire thing twice, but hey

def file_sort(words_dic):
    '''
    this uses one parameter- the dictonary from the previous function-
    and sorts all the contents of the file into the distinctions we
    have. notable mentions- storage and greatest_used work in tandem to store
    the greatest used words and the number of times they were used respectively.
    storage[3] stores the total number of unique words
    all the other lists are fairly self-explanatory.

    Note:
    line 118: # yes, this counts all capital letters
                #print(j) ## even if they're not at the start of the word, but
                ## honestly if someone's writing lIkE tHiS they deserve
                ## to have their data messed up. Also, using i[0] wasn't
                ## an option because you can sometimes have multiple spaces at once-
                ## which would create a list/dictionary entry with no length,
                #3 which would crash the program. this is the only workaround
                ## that worked
    '''
    storage, is_capital, is_not_capital, is_punctuated = [0, 0, 0, 0], [], [], []
    isnt_punctuated, punctuation, capital, greatest_used = [], [0,0], [0,0], ['','','']
    for i in words_dic: ## starts iterating through the entire dictionary
        #storage[3]+=1 ## total unique words
        ## this entire bit gets the greatest used words for each word type
        if len(i)<=4: ## short words. note: 0th index in both storage and
            if words_dic[i]>storage[0]: # greatest_used is for short words
                greatest_used[0]=i
                storage[0]=words_dic[i]
        elif len(i)>=5 and len(i)<=7: ## medium words, 1st index
            if words_dic[i]>storage[1]:
                greatest_used[1]=i
                storage[1]=words_dic[i]
        elif len(i)>=8: ## long words, second index
            if words_dic[i]>storage[2]:
                greatest_used[2]=i
                storage[2]=words_dic[i]
        for j in i: ## iterates through the letters of the words
            if j.isupper()==True:
                if i not in is_capital: ## checks to make sure it's unique
                    capital[0]+=1 ## adds to capital count
                    is_capital.append(i) ## makes sure we don't have duplicates
            else:
                if i not in is_not_capital: ## not capital
                    capital[1]+=1 ## same thing
                    is_not_capital.append(i)
        if ',' in i or '.' in i or '?' in i or '!' in i: ## is it punctuated
            ##print(i)
            if i not in is_punctuated: #3 removes duplicates
                punctuation[0]+=1 ## updates count
                is_punctuated.append(i) ## avoids duplicates
        if ',' not in i or '.' not in i or '?' not in i or '!' not in i:
            if i not in isnt_punctuated: #3 same thing
                punctuation[1]+=1
                isnt_punctuated.append(i)
    storage[3]=len(words_dic)
    return capital, punctuation, is_punctuated, \
        isnt_punctuated, words_dic, greatest_used, storage


def word_len_function(capital, punctuation, is_punctuated, isnt_punctuated, \
    words_dic, greatest_used, storage):
    '''
    this imports a whole lot of parameters, but
    since we can't use global variables we're just gonna
    have to roll with it. it counts the number of small,
    medium and big words and sorts them into neat categories.
    it returns a few dictionaries, that are then passed into the next
    function

     edit: good. god. we're supposed to keep the punctuation as
     it contributes to the word length. oh. my. lord. I spent
     so much time on this code (now deleted, because comments in code
     count towards the function length. it was like 30 lines). guys please
     PLEASE MENTION STUFF LIKE THIS.
    '''
    word_list=[]
    small_words=[]
    medium_words=[]
    big_words=[]

    ## lists to contain the number of times each word has occured

    for i in words_dic:
        if len(i)<5: ## small words ## appends no. of times
            small_words.append(words_dic[i]) ## word has appeared into the list
        elif len(i)>=5 and len(i)<=7: ## med words
            ##print(word_list[i])
            medium_words.append(words_dic[i])
        elif len(i)>=8: ## big words
            big_words.append(words_dic[i])

    return storage_for_formatting(small_words, medium_words, big_words, \
        capital, punctuation, word_list, greatest_used, storage)

def storage_for_formatting(small_words, medium_words, big_words, \
    capital, punctuation, word_list, greatest_used, storage):
    '''
    sister function to word_len_function, only here because of the
    30 line cap on functions. it accepts a lot of the parameters
    from word_len_function because they were originally
    supposed to only be the one function. it calculates percentages,
    and returns the percentages along with all the things word_len_function
    calculated because, and i cannot stress this enough, they are the same
    function painstakingly split into two to avoid the penalty for
    exceeding the completely arbitrary 30-line limit on functions
    '''
    small_words_no=0
    med_words_no=0
    big_words_no=0
    for i in small_words: ## just counts up how many small
        small_words_no+=1 ## medium and big words there are
    for i in medium_words: ## using dictionaries
        med_words_no+=1
    for i in big_words:
        big_words_no+=1
    total_words_no=small_words_no+med_words_no+big_words_no

    '''
    this function looks a bit bare and short, doesn't it?
    that's because all this stuff was supposed to tally up something
    different, but then it was clarified to me in office hours that
    we weren't supposed to do that. just please, make the documentation
    as verbose and as detailed as you expect our comments to be
    '''

    percentage=[0]*7 ##tallies up all percentages
    percentage[0]=float(small_words_no/(total_words_no)) ##percent small
    percentage[1]=float(med_words_no/(total_words_no)) ## percent medium
    percentage[2]=float(big_words_no/(total_words_no)) ## percent large
    percentage[3]=float(capital[0]/(capital[0]+capital[1])) ## percent capital
    percentage[4]=float(capital[1]/(capital[0]+capital[1])) ## percent not capital
    percentage[5]=float(punctuation[0]/(punctuation[0]+punctuation[1])) ## percent punctuated
    percentage[6]=float(punctuation[1]/(punctuation[0]+punctuation[1])) ## percent not punctuated
    return percentage, greatest_used, storage, word_list

def graphics_stuff(percentage, name, greatest_used, storage, word_list):
    '''
    this is the final function. it takes one parameter from main (name)
    and all the others from word_len_function. it processes these parameters and
    passes them into some functions that were made because of the 30-line limit
    on functions. i'd whinge, but i'm far too tired. it does not return anything
    '''
    from graphics import graphics
    gui=graphics(650, 700, 'infographic')
    word_counts=(str(greatest_used[0]) , '(' + str(storage[0]) +'x' + ')' ,\
        str(greatest_used[1]) , '(' + str(storage[1]) +'x' + ')' , \
        str(greatest_used[2]) , '(' + str(storage[2]) +'x' + ')') ## formatting
        ## everything for a seamless printing experience
    #print(percentage)
    gui.rectangle(0,0,650,700, 'grey') #background
    bar_graphs(gui, percentage)
    text_display(gui, percentage, storage, name, greatest_used, word_counts)

def bar_graphs(gui, percentage):
    '''
    accepts parameters gui and percentage from graphics_stuff, and uses them
    to create proportional bar graphs. it does not return any values, but simply
    outputs to the gui.
    '''
    i=450 #height of bar graphs
    ## lengths
    gui.rectangle(30,200, 150,i*percentage[0], 'light blue') #small
    gui.rectangle(30, i*percentage[0]+200, 150, i*percentage[1], 'light green') ## mid
    gui.rectangle(30, i*percentage[1]+i*percentage[0]+200, 150, i*percentage[2], 'light blue') ## long

    ## word capitalization
    gui.rectangle(220,200, 150,i*percentage[3], 'light blue') #capital
    gui.rectangle(220, i*percentage[3]+200, 150, i*percentage[4], 'light green') ## not capital

    ## word punctuation
    gui.rectangle(420,200, 150,i*percentage[5], 'light blue') ## punctuated
    gui.rectangle(420, i*percentage[5]+200, 150, i*percentage[6], 'light green') ## not punctuated

def text_display(gui, percentage, storage, name, greatest_used, word_counts):
    '''
    accepts parameters from graphics_stuff and some variables, and formats them into
    some text displays that it then outputs to the screen. it does not return any values,
    '''
    i=450 #height of bar graphs

    ## text displays that vary
    if percentage[0]!=0:
        gui.text(32,200, 'small words', fill='black', size=10) #small
    if percentage[1]!=0:
        gui.text(32,i*percentage[0]+200, 'medium words', fill='black', size=10)
    if percentage[2]!=0:
        gui.text(32,i*percentage[0]+200+i*percentage[1], 'long words', fill='black', size=10)
    if percentage[3]!=0:
        gui.text(227,200, 'Capitalized', fill='black', size=10)
    if percentage[4]!=0:
        gui.text(227,i*percentage[3]+200, 'Non Capitalized', fill='black', size=10)
    if percentage[5]!=0:
        gui.text(422,200, 'Punctuated', 'black', size=10) ## punctuated
    if percentage[6]!=0:
        gui.text(422,i*percentage[5]+200, 'Non-Punctuated', 'black', size=10)

    #3 text display that doesn't vary
    gui.text(31, 31, name, fill='light green', size=20) ## file name
    gui.text(30, 30, name, fill='light blue', size=20) ## file name but make it funky
    gui.text(30, 70, 'Total Unique Words: ', fill='white', size=20) ## total unique words
    gui.text(290, 70, storage[3], fill='white', size=20)
    gui.text(30, 110, 'Most used words (s/m/l):', fill='white', size=12) ## most used words
    gui.text(220, 110, word_counts, fill='light blue', size=12)
    gui.text(31, 160, 'Word lengths', fill='white', size=20) ## word lengths
    gui.text(220, 160, 'Cap/Non-Cap', fill='white', size=20) ## cpitalization
    gui.text(420, 160, 'Punct/Non-Punct', fill='white', size=20) ## not capitalized

main()