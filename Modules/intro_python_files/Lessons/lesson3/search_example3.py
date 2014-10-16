#! /usr/local/bin/python3

def searchProducts():

    f = open('searchexample.txt','r+')

    searchTool = input("What tool do you want to search for?")

    for line in f:
        if searchTool in line:
            print(line)
            print('£',next(f,''),end='')
            print('quantity available:',next(f,''),end='')
            break
        
    
    f.close()

searchProducts()
