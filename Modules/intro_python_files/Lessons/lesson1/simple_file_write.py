#! /usr/local/bin/python3

f = open('workfile.txt','w')    #opens a file with write access

for x in range (1,11):          #sets up a for loop to print values from 1 to just before 11
	f.write(str(x))         #each time it loops through the for loop it writes the value of x as a string	
	f.write('\n')           #writes a new line

f.close()                       #closes the file - must always do this!
