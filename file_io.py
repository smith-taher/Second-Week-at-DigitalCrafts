#1. Write a program that prompts the user to enter a file name, reads the contents of the file and prints it to the screen
# fileName = raw_input("Enter a filename: ")
# file = open(fileName, 'r')
# print file.read()
# this code is working

#2. Write a program that prompts the user to enter a file name, then prompts the user to enter the contents of the file, and then saves
#the content to the file.
fileName = raw_input("Enter a filename: ")
file = open(fileName, 'a+')
newContents = raw_input("Enter new contents: ")
file.write(newContents)
file.seek(0)
print file.read()
#file.close()

#3. Write a program that prompts the user to enter a file name, then prints the letter histogram and the word histogram
#of the conents of the file.