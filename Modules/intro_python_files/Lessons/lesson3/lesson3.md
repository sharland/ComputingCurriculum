# Searching Python Files

##Lesson number *3* of *y*

##Lesson objective

##Lesson description

```python
#! /usr/local/bin/python3

f = open('searchexample.txt','r')

searchTool = input("What tool do you want to search for?")

lines = f.read()
charStart = lines.find(searchTool)
if charStart == -1:
    print (searchTool,'is not in the file')
else:
    print (searchTool,'is in the file')
```

