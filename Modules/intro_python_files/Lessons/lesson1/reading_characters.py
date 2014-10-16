#! /usr/local/bin/python3

f = open('examplefile.txt','r')    #opens a file with write access
print("Printing characters 1, 3 and 7 from the file")
print(f.read(1))
print(f.read(3))
print(f.read(7))
f.close()
