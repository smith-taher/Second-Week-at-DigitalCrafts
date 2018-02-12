# ---saved the database---
import pickle, os



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
   print '5. Save entries'
   print '6. Restore saved entries'
   print '7. Quit'
   #print()


menu_choice = 0

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.phone, self.email)

phoneBook = []

def reStore():
    global phoneBook
    if os.path.isfile('phonebook_file.pickle') == True:
        phonebook2 = open('phonebook_file.pickle', 'r+')
        phoneBook = pickle.load(phonebook2)
        phonebook2.close()
    else:
        phoneBook = []

while menu_choice != 7:
    print_menu()
    menu_choice = int(raw_input('What do you want to do? (1-5): '))
    if menu_choice == 1:
        lookupname = raw_input('Name: ')
        if len(phoneBook) != 0:
            for i in phoneBook:
                if i.name == lookupname:
                    print i
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
        def getSomethingToSortBy(phoneBook):
            return phoneBook.name
        sorted_phonebook = sorted(phoneBook, key=getSomethingToSortBy)
        print sorted_phonebook
        # for x in phoneBook:
        #     sorted(phoneBook) 
        #     print phoneBook
            #print 'Found entry for %s' % Contacts(phoneBook)
    elif menu_choice == 5:
        # open the file in write mode (w)
        myfile = open('phonebook_file.pickle', 'w+')
        # dump the contents of the phonebook_dict into myfile - the open file
        pickle.dump(phoneBook, myfile)
        # close myfile
        myfile.close()
        print '%s has been saved' % name
    elif menu_choice == 6:
        reStore()
        print phoneBook
    elif menu_choice != 7:
        print_menu()
print 'Bye.'








#from Web
#!/usr/bin/python
#filename address-book.py
# import pickle
# import os
# class Contact:
#     def __init__(self,name,email,phone):
#         self.name=name
#         self.email=email
#         self.phone=phone
        
#     def __str__(self):
#         return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name,self.email,self.phone)
        
#     def change_name(self,name):
#         self.name=name
        
#     def change_email(self,email):
#         self.email=email
        
#     def change_phone(self,phone):
#         self.phone=phone
        
# def add_contact():
#     address_book_file=open("address_book_file","r")
#     is_file_empty=os.path.getsize("address_book_file")==0
#     if not is_file_empty:
#         list_contacts=pickle.load(address_book_file)
#     else:
#         list_contacts=[]
#     try:
#         contact=get_contact_info_from_user()
#         address_book_file=open("address_book_file","w")
#         list_contacts.append(contact)
#         pickle.dump(list_contacts,address_book_file)
#         print "Contact added"
#     except KeyboardInterrupt:
#         print "Contact not added"
#     except EOFError:
#         print "Contact not added"
#     finally:
#         address_book_file.close()
    
# def get_contact_info_from_user():
#     try:
#         contact_name=input("Enter contact name\n")
#         contact_email=input("Enter contact email\n")
#         contact_phone=input("Enter contact phone number\n")
#         contact=Contact(contact_name,contact_email,contact_phone)
#         return contact
#     except EOFError as e:
#         #**print "You entered end of file. Contact not added"
#         raise e
#     except KeyboardInterrupt as e:
#         #**print "Keyboard interrupt. Contact not added"
#         raise e
    
# def display_contacts():
#     address_book_file=open("address_book_file","r")
#     is_file_empty=os.path.getsize("address_book_file")==0
#     if not is_file_empty:
#         list_contacts=pickle.load(address_book_file)
#         for each_contact in list_contacts:
#             print each_contact
#     else:
#         print "No contacts in address book"
#         return
#     address_book_file.close()
    
# def search_contact():
#     #**search_name=input("Enter the name\n")
#     address_book_file=open("address_book_file","r")
#     is_file_empty=os.path.getsize("address_book_file")==0
#     if not is_file_empty:
#         search_name=input("Enter the name\n")
#         is_contact_found=False
#         list_contacts=pickle.load(address_book_file)
#         for each_contact in list_contacts:
#             contact_name=each_contact.name
#             search_name=search_name.lower()
#             contact_name=contact_name.lower()
#             if(contact_name==search_name):
#                 print each_contact
#                 is_contact_found=True
#                 break
#         if not is_contact_found:
#             print "No contact found with the provided search name"
#     else:
#         print "Address book empty. No contact to search"
#     address_book_file.close()

# def delete_contact():
#     #**name=input("Enter the name to be deleted\n")
#     address_book_file=open("address_book_file","r")
#     is_file_empty=os.path.getsize("address_book_file")==0
#     if not is_file_empty:
#         name=input("Enter the name to be deleted\n")
#         list_contacts=pickle.load(address_book_file)
#         is_contact_deleted=False
#         for i in range(0,len(list_contacts)):
#             each_contact=list_contacts[i]
#             if each_contact.name==name:
#                 del list_contacts[i]
#                 is_contact_deleted=True
#                 print "Contact deleted"
#                 address_book_file=open("address_book_file","w")
#                 if(len(list_contacts)==0):
#                     address_book_file.write("")
#                 else:
#                     pickle.dump(list_contacts,address_book_file)
#                 break
#         if not is_contact_deleted:
#             print "No contact with this name found"
            
#     else:
#         print "Address book empty. No contact to delete"
#     address_book_file.close()
    
# def modify_contact():
#     address_book_file=open("address_book_file","r")
#     is_file_empty=os.path.getsize("address_book_file")==0
#     if not is_file_empty:
#         name=input("Enter the name of the contact to be modified\n")
#         list_contacts=pickle.load(address_book_file)
#         is_contact_modified=False
#         for each_contact in list_contacts:
#             if each_contact.name==name:
#                 do_modification(each_contact)
#                 address_book_file=open("address_book_file","w")
#                 pickle.dump(list_contacts,address_book_file)
#                 is_contact_modified=True
#                 print "Contact modified"
#                 break
#         if not is_contact_modified:
#             print "No contact with this name found"
#     else:
#         print "Address book empty. No contact to delete"
#     address_book_file.close()
    
# def do_modification(contact):
#     try:
#         while True:
#             print ("Enter 1 to modify email and 2 to modify address and 3 to quit without modifying")
#             choice=input()
#             if(choice=="1"):
#                 new_email=input("Enter new email address\n")
#                 contact.change_email(new_email)
#                 break
#             elif(choice=="2"):
#                 new_phone=input("Enter new phone number\n")
#                 contact.change_phone(new_phone)
#                 break
#             else:
#                 print "Incorrect choice"
#                 break
#     except EOFError:
#         print "EOF Error occurred"
#     except KeyboardInterrupt:
#         print "KeyboardInterrupt occurred"
    
# def print_menu():
#     print '====================='
#     print 'Electronic Phone Book'
#     print '=====================' 
#     print '1. Look up an entry'
#     print '2. Set an entry'
#     print '3. Delete an entry'
#     print '4. List all entries'
#     print '5. Quit'
#     print 
# # **print "Enter 'a' to add a contact, 'b' to browse through contacts, 'd' to delete a contact, 'm' to modify a contact, 's' to search for contact and 'q' to quit"
# while True:
#     print_menu()
#     menu_choice = int(raw_input('What do you want to do? (1-5): '))
#     #**choice=input("Enter your choice\n")
#     if menu_choice == 5:
#         break
#     elif menu_choice == 2:
#         add_contact()
#     elif menu_choice == 4:
#         display_contacts()
#     elif menu_choice == 3:
#         delete_contact()
#     elif menu_choice == 8:
#         modify_contact()
#     elif menue_choice == 1:
#         search_contact()
#     else:
#         print "Incorrect choice. Need to enter the choice again"

#from Web
# """write info out to a text file - how to do this is in code academy at the end (input/output)
# also probably create an address book class which saves all the info and has a "write to file" method
# that writes the address to the file.
# if has another method which can search the file and return an address if given a name or address or phone etc
# global variables may help?"""

# name = raw_input("What would you like to call your address book?")+".txt"
# c = open(name, "a")
# print open(name, "a")


# def main_menu():
#     # This initiates the address books and allows users to select which feature to use
#     choice = raw_input("Press 1 to view your contacts, 2 to enter a new contact and 3 to search your contacts")
#     if choice == "1":
#         c = open(name, "r")
#         file_contents = c.read()
#         print (file_contents)
#         c.close
#     elif choice == "2":
#         enter_contacts()
#         main_menu()
#     elif choice == "3":
#         search_contacts()
#         main_menu()


# def search_contacts():
#     # Searches contact list
#     choice = raw_input("Search for a contact by any kind of information: ")
#     c = []
#     c = list(contact)
#     for line in range(0, len(list)):
#         if choice in line:
#             print line
#         else:
#             choice = raw_input("There's no one named " + choice + " in your contact list. Press 2 to enter them now")
#             if choice == "2":
#                 enter_contacts()
#             else:
#                 print "Please choose an item from the menu"


# def clean_first():
#     # Ensures that the first name of a user is capitalized
#     # Ensures that only legal names are accepted in this field
#     one = raw_input("First name ")
#     f = one[1:10]
#     g = one[0]
#     return g.upper() + f


# def clean_last():
#     # Ensures that the first name of a user is capitalized
#     # Ensures that only legal names are accepted in this field
#     two = raw_input("Last name ")
#     a = two[1:10]
#     b = two[0]
#     return b.upper() + a


# def clean_phone():
#     # Takes a 10 digit input and presents it in the [(###) ###-####] format
#     # Avoids mistakes & stupidity surrounding 10-digit phone numbers
#     phone = raw_input('Phone number with area code ')
#     if (len(phone) == 10) and phone[0:len(phone)] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
#         telephone = "1 " + "(" + phone[0:3] + ")" + " " + phone[3:6] + "-" + phone[6:10]
#     else:
#         telephone = "Only numerals are accepted in this field"
#     return telephone


# def clean_media():
#     # Presents a contact's social media in a clean manner, with an @ symbol
#     # Avoids
#     media = raw_input('Social media ')
#     if 15 >= len(media) - 1:
#         social = "@" + media
#     else:
#         social = "Social media handles must be 15 characters or less"
#     return social


# def clean_mail():
#     # Ensures that an email is valid before allowing a user to assign it to a contact
#     addie = raw_input('E-mail ')
#     return addie


# def enter_contacts():
#     # Collects contact info
#     # Saves contact info to a list
#     f = clean_first()
#     last = clean_last()
#     telephone = clean_phone()
#     email = clean_mail()
#     addie = raw_input('Address ')
#     social = clean_media()
#     contact = ("[" + f + " " + last + "|" + telephone + "," + email + "|" + addie + " " + social + "]")
#     with open(name, "a") as text_file:
#         text_file.write(contact)
#     print "The contact " + contact + " has been added to your address book"

# main_menu()
