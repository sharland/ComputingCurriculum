# Introduction to Python Files

## Lesson number *1* of *y*

## Lesson objective

In this lesson we will take a look at the basics of Python Files

## Lesson description

### Introduction 

Python handles variables really well.  We've seen them being used in many ways so far but ultimately they only store data within that python script which isn't accessible when the script stops running.  What we are going to look at now is how to use Python Files to store data in a separate location to the python script.  This is useful as any data which is stored there is obviously accessible once the program finishes running.

This also means it might be possible to generate content which could be used in a completely different script or even a completely different language!

### Setting up a simple read and write file

In the same folder as this file are two python scripts for reading and writing.  We will start with the writing file:

```python
#! /usr/local/bin/python3

f = open('workfile.txt','w')    #opens a file with write access

for x in range (1,11):          #sets up a for loop to print values from 1 to just before 11
	f.write(str(x))         	#each time it loops through the for loop it writes the value of x as a string	
	f.write('\n')           	#writes a new line

f.close()                       #closes the file - must always do this!
```

**Points to consider:**

All files should obviously be opened.  By opening it and assigning that open file to a variable you can then continue to refer to that open file object using the variable name.  The function `open` then has two arguments which are the name of the file to open and the access mode (more on that below)

**Cool thing that happens:**  If you state the name of the file to open and the file doesn't already exists python will create that file for you.  As explained in the table below this only happens if the file access mode is set to `"w"` or `"w+"` or `"a+"`.

The following table shows the file access modes which you can apply in the second argument for the function `open`.

**Text File Access Modes**
|Mode|Description|
|---|---|
|`"r"`|Read from a text file.  If the file is not there, Python will complain with an error.|
|`"w"`|Write to a text file.  If the file is there, the contents will be overwritten.  If the file isn't there it will be created|
|`"a"`|Read from and write to a text file.  Just like read access Python will complain if the file isn't there.|
|`"r+"`|Write to and read from a file.  If the file is there the contents will be written over.  If the file is not there Python will produce an error|
|`"w+"`|Write to and read from a text file.  If the file is there, the contents will be overwritten.  If the file isn't there it will be created.|
|`"a+"`|Append to and read from a text file.  If the file is there, new data is appended to it.  If not, the file is created.|

Closing the file is very important at the end of the script and you would use the variable name representing the text file followed by the method `close()`.

```python
f.close()
```

### Exercise

Open the `simple_file_read.py` and `simple_file_write.py` files and play around with them.  Note down what they are doing and then try and change some code.  If you want to make a few changes it might be a good idea to make a copy of the file before you change it.

### Things you can do when reading a file

We are now going to go through a number of things you can do when reading a text file in python.  All scripts refer to the same text file called `examplefile.txt` which contains a list of fruit.  This is so that you can compare the output from each script.

1. Reading characters from a file
2. Reading characters from a line
3. Reading one line at a time
4. Reading specific lines
5. Reading the whole file
6. Reading the entire file into a list
7. Reading specific lines into a list

### 1. Reading characters from a file

Example code:
```python
#! /usr/local/bin/python3

f = open('examplefile.txt','r')    #opens a file with write access
print("Printing characters 1, 3 and 7 from the file")
print(f.read(1))
print(f.read(3))
print(f.read(7))
f.close()
```
When running the above you should get the following output:
```
Printing characters 1, 3 and 7 from the file
a
ppl
e
mango
```
The `a` shows that it has read the first character.  The `ppl` shows that it has read the next 3 characters.  The `e` followed by the `mango` on the next line shows that it has read the next 7 characters.  As `mango` is written in the file on a new line this is why it appears on a separate line when printed.  If you count the number of characters produced from `print(f.read(7))` you will also see that it does not equal 7.  This is because the read method is probably counting an invisible character at the end of the `apple` line showing that a new line has been made.

If you continue to write `print(f.read(n))` lines where n is represented by a number you will simply continue reading characters from where the previous line finished.  If you want to start at the beginning again in the same python script you can simple close the file and re-open it.

