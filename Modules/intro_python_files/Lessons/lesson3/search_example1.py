#! /usr/local/bin/python3

f = open('searchexample.txt','r')

searchTool = input("What tool do you want to search for?")
searchLength = len(searchTool)

lines = f.read()
charStart = lines.find(searchTool)
if charStart == -1:
    print (searchTool,'is not in the file')
else:
    print (searchTool,'is in the file')
    f.seek(0,0)
    for line in f:
        if searchTool in line:
            print(next(f,''),end='')
    
f.close()
