#! /usr/local/bin/python3

f = open('workfile.txt','r')    #opens a file with read access

for x in range (1,11):          #sets up a for loop to print values from 1 to just before 11
	f.read(x)               #reads what the value of x is	
	print(x)                #prints what it finds

f.close()                       #closes the file - must always do this!
