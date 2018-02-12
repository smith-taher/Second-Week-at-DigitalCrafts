# ---saved the database---
# import pickle
#...
# open the file in write mode (w)
# myfile = open('phonebook.pickle', 'w')
# dump the contents of the phonebook_dict into myfile - the open file
# pickle.dump(phonebook_dict, myfile)
# close myfile
# myfile.close()

#---restore the saved entries---
# open the file in read mode (r)
# myfile = open('phonebook.pickle', 'r')
# load the contents from the file and store it in the phonebook_dict variable
# phonebook_dict = pickle.load(myfile)


def print_menu():
   print '====================='
   print 'Electronic Phone Book'
   print '=====================' 
   print '1. Look up an entry'
   print '2. Set an entry'
   print '3. Delete an entry'
   print '4. List all entries'
   print '5. Quit'
   #print()

phoneBook = []
menu_choice = 0

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.phone, self.email)

while menu_choice != 5:
    print_menu()
    menu_choice = int(raw_input('What do you want to do? (1-5): '))
    if menu_choice == 1:
        lookupname = raw_input('Name: ')
        if len(phoneBook) != 0:
            for i in phoneBook:
                if i.name == lookupname:
                    print i
            # if lookupname == phoneBook[0]:
            #     print 'Found entry'
        # if name in Contact(name):
            # print 'Found entry' 
            # %s - Phone: %s - Email: %s' % (self.name, self.phone, self.email)
        else:
            print 'That name was not found :('
    elif menu_choice == 2:
        name = raw_input('Name: ')
        phone = raw_input('Phone #: ')
        email = raw_input('Email: ')
        newContact = Contact(name, phone, email)
        phoneBook.append(newContact)
        print 'Entry stored for %s' % name
        # print phoneBook
    elif menu_choice == 3:
        lookupname = raw_input('Name: ')
        for i in phoneBook:
            if i.name == lookupname:
                phoneBook.remove(i)
                print 'Deleted entry for %s' % lookupname
            else:
                print '%s was not found' % lookupname
    elif menu_choice == 4:
        for x in phoneBook:
            sorted(phoneBook) 
            print phoneBook
            #print 'Found entry for %s' % Contacts(phoneBook)
    elif menu_choice != 5:
        print_menu()
print 'Bye.'






