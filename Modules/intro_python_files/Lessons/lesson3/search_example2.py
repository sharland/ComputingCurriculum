#! /usr/local/bin/python3

searchTool = input("What tool do you want to search for?")

with open('searchexample.txt') as file:
    for line in file:
        if searchTool in line:
            print(next(file, ''), end='')
    
file.close()
