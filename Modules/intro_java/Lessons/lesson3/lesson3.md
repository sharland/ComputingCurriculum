#Lesson Template

##Lesson Title

##Lesson number *x* of *y*

##Lesson objective

In this lesson we will look at the use of Java packages and classes

##Lesson description

A java package is a folder which contains a group of related programs.

[Java packages you can work with](http://docs.oracle.com/javase/8/docs/api/)

Take a look down the list of packages for java.util and for a class in there called random.  In random is a method called nextint which can be used to generate random integers

To access that program use the following example code ...

```java
import java.util.*; //the wild card gives access to all of the classes in that folder

public class ClassNameHere {

	public static void main (String[] Args) {
	
	
	
	} // end main method
	
} // end main class
```

If you want to access only the one class use `import java.util.Random;` instead.

A reminder that a class is essentially a blueprint of an object.  A blueprint has all the detail describing how an object might look like but it is still a plan.  We can't use the object until we build it from a class same as how you use a blueprint to build a house.

We start building by using the name of the class.  We then give the object a name which is unique to that object.  We then assign it all of what was in that class (variables and methods) to that object. 

So here is a class ...
```java
public class House() {
	
}//end class
```
and we build it into an object through ...
```java
House house1 = new House();
```

An example using the java.util package classes would therefore be ...
```java
import java.util.Random;

public class ClassName {

	public static void main (String[] Args) {
	
	Random randomNumber = new Random();
	
	}//end main method
	
}//end main class
```
We can then create multiple objects from the same class using different behaviours or attributes for each object.