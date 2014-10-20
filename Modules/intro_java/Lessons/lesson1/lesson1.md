# What is Java?

## Lesson number *1* of *y*

## Lesson objective

Introduce pupils to general concepts of Java as a programming language and complete our first application - a HelloWorld script.

## Lesson outline

Most links are to supporting wikipedia articles to encourage further reading.

### What is Java?

[Java](http://en.wikipedia.org/wiki/Java_(programming_language)) is both a programming language and platform.

[Programming language](http://en.wikipedia.org/wiki/Computer_programming_language): A method of writing instructions for a computer to follow using a range of conventions

[Platform](http://en.wikipedia.org/wiki/Computing_platform): A platform is a virtualised version of a system running inside another system which runs its own code.

[Virtualised](http://en.wikipedia.org/wiki/Virtualization): something is run on a computer system as if it is installed but it is encapsulated away from the rest of the system.

### What sort of language is Java?

Java is a high-level programming language.  It is also simple, architecture neutral, Object Orientated, Portable, distributed, High performance, multi-threaded, Robust, Dynamic, secure, multi-paradigm, structured, imperative, functional, generic, reflective and concurrent.

Some of these terms are defined below:

[high-level programming](http://en.wikipedia.org/wiki/High-level_programming_language): A programming language which uses language which we as humans can understand but a CPU may not.  When it is run it is compiled into a form which a CPU can understand.

architecture-neutral: java can be run on multiple types of computers and as it runs the same regardless of the system it is known as architecture-neutral.

[Object Orientated](http://en.wikipedia.org/wiki/Object-oriented_programming): This is a programming paradigm (way of doing things) which uses the concepts of 'objects' with 'data fields' that describe the object and associated procedures known as methods.  Objects interact with one another to form applications.  This will be covered many times as we move through learning how to use Java.

portable:  This simply means that Java can be run on multiple systems using the Java Virtual Machine.

distributed: This refers to objects which have been distributed across a network and with which a Java application can interact.

High-performance: Java has been known to be slow in the past due to running in a VM and not directly on the CPU but it has improved in speed in recent years.

[multi-threaded](http://www.tutorialspoint.com/java/java_multithreading.htm): A multi-threaded program contains two or more parts which can run concurrently and each part can handle different tasks at the same time.

robust: Java is robust as it is highly supported, portable and puts a lot of emphasis on early detection of errors.

[dynamic](http://en.wikipedia.org/wiki/Dynamic_programming): Dynamic programming is a method of solving complex problems by breaking them down into smaller sub-problems.

[secure](http://en.wikipedia.org/wiki/Java_security): Java has a number of security features chief amongst them being the ability to sandbox code (running code without access to anything else).  Read the wiki link for more info.

[multi-paradigm](http://en.wikipedia.org/wiki/Multi-paradigm_programming_language#Multi-paradigm): Java supports multiple paradigms (ways in which programmers can do things).  This provides flexibility to the system and to the programmer.

[Structured](http://en.wikipedia.org/wiki/Structured_programming): This is a programming paradigm which provides a structure for how code is used and written.  This is to make the code clearer and better quality.  It uses clear subroutines, block structures and for and while loops.

[imperative](http://en.wikipedia.org/wiki/Imperative_programming): This is another programming paradigm which describes computation in terms of actions which change the programs state.  In other words it prescribes how to perform an action rather than declare what needs to be done.

[functional](http://en.wikipedia.org/wiki/Functional_programming): This is another programming paradigm which describes functions that produce results that depend on inputs and not on the current state of the program.

[generic](http://en.wikipedia.org/wiki/Generic_programming): When you declare a class as a template you don't worry about what type of data will be handled by the operations of the class.  This is known as generic programming.

[reflective](http://en.wikipedia.org/wiki/Reflective_programming):  This is the ability of a program to examine and modify the structure and behaviour of the program at runtime.

## How is code written in Java

In Java all source code can be written as plain text files ending with the .java extension.  These are compiled into .class files by the javac compiler.

The .class file contains code not for the machine code of your processor but instead it contains bytecodes for the Java Virtual Machine.  The Java launcher tool will then run your code within an instance of the JVM.

This means that .class files can be compiled and run on any system which can run a Java Virtual Machine.  This gives you the ability to write a .class file which can then be run in the same way on many machines.  This gives a very high level of compatibility for your code also known as 'write once, run anywhere'.

## The Java Platform

A platform is a combination of software and hardware.  The JVM is the base of a software platform which runs on top of a hardware platform.  This means that the JVM can be run on a number of operating systems.

When you would with Java you will also be working with a Java API.  This is a collection of of software components which improve the capabilities of Java.  These are presented as libraries of classes and interfaces.

## A general summary of what Java can do

1.  *Development tools*
  * All the tools for compiling, running, monitoring, debugging and documenting your applications.
2.  *Application Programming Interface*
  * This is the core functionality of the Java language with a wide range of classes ready for your use in multiple ways.
3.  *Deployment technologies*
  * Once your code is complete these are used to deploy your code to your customers and clients.
4.  *User Interface toolkits*
  * Using toolkits like Swing and Java 2D it is possible to create useful GUI frontends for your java app.
5.  *Integration libraries*
  * A range of integration libraries provide database access and manipulation of remote objects

## Activity - program the 'Hello World' Application

These instructions are written using Eclipse on a Mac.

1. Download and install Eclipse from [here](http://www.eclipse.org)
2. Change the perspective to Java by going to *Window > Open perspective > Java*.  A perspective in Eclipse enables different types of tasks to be worked on such as working in Java or focussing on debugging.  It is likely that Eclipse will open in the Java perspective in any case as it will be set as default.
*Changing perspective*
![Change perspective](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/eclipse1.jpg)
*Changing perspective*
![Change perspective](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/eclipse2.jpg)
[YouTube video tutorial showing how to change perspective](https://www.youtube.com/watch?v=3ak3i_AOE9w)
3. Create a new Java project by clicking on *File > New > New Java Project* or the new Java project button in the toolbar.  Input the project name 'HelloWorld' (without quotes) and click finish.  We now have somewhere to essentially manage our new project.
*New project selection*
![New project selection](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/new%20project.jpg)
*Add a project name*
![Add a project name](https://github.com/sharland/IntroToJava/raw/master/Lessons/lesson1/name%20new%20project.jpg)
[Youtube video on setting up new project in Eclipse](https://www.youtube.com/watch?v=PGpneRQsenE)
4. Create a new class (we will start looking at classes in the next lesson) by selecting the 'New Class' button (available in at least 3 places!).  In the dialogue box which appears make sure `HelloWorld/src` is specified as the source folder and then select the checkbox to create the `main()` method and click finish.  Your first Java code will appear.
*Selecting a new class*
![Select new class](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/new%20class.jpg)
*Setting up the new class*
![Setup new class](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/setup%20class.jpg)
*Class created*
![Class created](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/class%20created.jpg)
[Youtube video on setting up a new class](https://www.youtube.com/watch?v=eRNHTjfeKx4)
```java

public class HelloWorld {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
	}

}
```
5. Add the following line to the `main()` method:
```java
			System.out.println("Hello world!");
```
Right click the class name and select *Run as > Java Project* and you should see the console window show the contents of your print statement.
*Adding a print statement*
![Add a print statement](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/add%20print%20statement.jpg)
*Run as Java application*
![Run as java application](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/run%20as%20java%20project.jpg)
*Console output shown*
![Console output](https://raw.githubusercontent.com/sharland/IntroToJava/master/Lessons/lesson1/console%20output.jpg)
[Youtube video on adding a print statement and running](https://www.youtube.com/watch?v=W1frArZi-y0)

### Summary

In today's lesson you have learnt some of the basics about what Java is and how to work with it.  You have also been able to successfully create and run your first Java application.
 