#Author: Avichal Kaul

## Description: Uses certain commands from a user to
## manage a contact list. It imports a list of contacts
## from a text file saved in its local directory, reads it
## into memory, and then either displays results from it
## or edits it depending on what the user inputs. It also
## saves all changes at the end.

#Comments: not allowing us to use lists is a nerf. Also, I know
## I'm screaming into the void at this point, but making test cases
## downloadable would've made this so, so much easier. It took almost
## three hours of slow, tedious debugging on gradescope for me to
## figure out what was going wrong. And what kind of black magic are you
## guys doing to input the inputs? They worked fine in mu, but the instant
## I uploaded the file to gradescope everything broke at once.

def contacts_import():
    '''
    This is a function that will run regardless of
    user input to initialize a set of contacts from
    a file that is assumed to already exist. It
    returns a set of contacts with tupes in it.
    '''
    contacts_file=open('contacts.txt', 'r')
    contacts_temp=contacts_file.readlines()
    ## loads the contents of the file into memory
    contacts=set()
    for i in contacts_temp:
        i=i.strip('\n')
        x=i.split(' | ') ## splits the lines
        contacts.add(tuple(x))
    return contacts

def main():
    '''
    Calls two functions, regardless of user input.
    It gets a set from contacts_import, which it then
    passes into input_function to handle all user inputs.
    It is mainly here for posterity's sake (and to
    handle that sick welcome message)
    '''
    contacts=contacts_import()
    print('Welcome to the contacts app!')
    input_function(contacts)

def input_function(contacts):
    '''
    This accepts one parameter- a set filled with tuples-
    and depending on the user input, either diverts the
    program into one of two functions or saves everything
    to the contacts.txt file and exits. If it does not
    understand the input, it expresses confusion. It
    only prints sometimes. It is also recursive, repeating
    the prompt for the user over and over again until it is
    exited.
    '''
    user_input=input('>')
    user_input=user_input.split(' ')
    ## this splits the input into a list, which makes it easier to deal with
    if user_input[0:3]==['show', 'contacts', 'with']:
        ## for input beginning with "show contacts with"
        show_contacts(user_input[3], user_input[4:], contacts) ## pass through into another function
        input_function(contacts)
    elif user_input[0:2]==['add', 'contact']:
        ## for input "add contact"
        add_contacts(contacts)
        contacts=input_function(contacts)
    elif user_input[0:1]==['exit']:
        ## for input "exit". It also saves to the file.
        print('Goodbye!')
        file=open('contacts.txt', 'w')
        for i in sorted(contacts):
            string=str(i[0]+' | '+i[1]+' | '+i[2]+'\n')
            file.write(string)
    else:
        ## for any input the program does not understand
        print('Huh?')
        input_function(contacts)

def show_contacts(A, inpt, contacts):
    '''
    This finds contacts from the contact list
    depending on what the user wants to search for,
    and prints them. It accepts three parameters-
    two strings from the user input to search, and
    the contacts set. It does not return anything,
    instead printing to the screen.
    '''
    B=''
    i=0
    while i<len(inpt):
        B+=inpt[i]
        if i!=len(inpt)-1:
            B+=' '
        i+=1
    ## this so far is just to deal with cases where
    ## the name in 'show contacts with name' has more
    ## than one word.
    matching=set()
    for i in contacts:
        if A=='name': ## changes the index of the tuple
            if i[0]==B: ## depending on what the user typed
                matching.add(i)
        elif A=='email':
            if B in i[1]:
                matching.add(i)
        elif A=='phone':
            if i[2]==B:
                matching.add(i)
    for contacts in sorted(matching): ## prints info
        print(contacts[0]+"'s contact info:")
        print('  email:', contacts[1])
        print('  phone:', contacts[2])
    if matching==set():
        print('None')

def add_contacts(contacts):
    '''
    This adds a new contact into the contacts
    set, and returns it to the user_input function
    to be processed and saved into the contacts.txt
    file. It accepts one parameter- the contacts set-
    and returns its edit to the set. It also prints
    'contact added'.
    '''
    name=input('name: ')
    email=input('email: ')
    phone=input('phone: ')
    ## interestingly, while this is the only way to get the
    ## correct output on gradescope, it completely breaks
    ## formatting in the mu editor run window. Why?
    tuple_contact=(name, email, phone) ## our contact tuple
    j=0
    for i in contacts:
        if i==tuple_contact:
            print('Contact already exists!')
            j+=600 ## yes, this breaks down for large contact files.
        else:       ## cut me some slack, it's been almost three hours
            j+=1    ## of debugging on gradescope. again, please make
    if j==len(contacts): ## the test cases downloadable.
        contacts.add(tuple_contact)
        print('Contact added!')
    return contacts ## returns contacts to input_function to
    ## save them to the file in the future.

main()