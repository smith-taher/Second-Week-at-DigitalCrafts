Hellodhfja;shdfjd!   print 'Electronic Phone Book'
   print '=====================' 
   print '1. Look up an entry'
   print '2. Set an entry'
   print '3. Delete an entry'
   print '4. List all entries'
   print '5. Quit'
   #print()

numbers = {}
name = {}                                       #added for sort
menu_choice = 0
#contacts = [name, numbers]                      #added for sort

while menu_choice != 5:
   print_menu()
   menu_choice = int(raw_input('What do you want to do? (1-5): '))
   if menu_choice == 1:
       name = raw_input('Name: ')
       if name in numbers:
           print 'Found entry for', name + ':', numbers[name]
       else:
           print name, 'was not found'
   elif menu_choice == 2:
       name = raw_input('Name: ')
       phone = raw_input('Number: ')
       numbers[name] = phone
       print 'Entry stored for', name
   elif menu_choice == 3:
       name = raw_input('Name: ')
       if name in numbers:
           del numbers[name]
           print 'Deleted entry for', name
       else:
           print name, 'was not found'
   elif menu_choice == 4:
       for x in numbers.keys():
            sorted(x)   #added for sorting
            print 'Found entry for', x + ':', numbers[x]    
   elif menu_choice != 5:
       print_menu()
print 'Bye.'


