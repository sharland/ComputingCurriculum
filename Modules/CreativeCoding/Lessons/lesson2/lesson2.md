# Starting to use Processing

## Lesson number *2* of *y*

## Lesson objective

- setup Processing
- complete first simple drawing tasks
- 

## Lesson description

Instructions to setup

1. use following code
```java
void setup() {
    size(500,500);
}
    
void draw() {
    background(0);
    ellipse(250,250,100,100);
}
```
2. add ControlP5 library (Sketch->Import Library->Add library)
3. setup example sketches from futurelearn
4. get pupils to work with some existing code
  - use
  ```java
  /*
 * Creative Coding
 * Week 1, 01 - Draw your name!
 * by Indae Hwang and Jon McCormack
 * Copyright (c) 2014 Monash University
 
 * This program allows you to draw using the mouse.
 * Press 's' to save your drawing as an image to the file "yourName.jpg"
 * Press 'r' to erase your drawing and start with a blank screen
 * 
 */


// setup function -- called once when the program begins
void setup() {

  // set the display window to size 500 x 500 pixels
  size(500, 500);

  // set the background colour to white
  background(255);

  // set the rectangle mode to draw from the centre with a specified radius
  rectMode(RADIUS);
}


// draw function -- called continuously while the program is running
void draw() {

  /* draw a rectangle at your mouse point while you are pressing 
   the left mouse button */

  if (mousePressed) {
    // draw a rectangle with a small random variation in size
    stroke(170); // set the stroke colour to a light grey
    fill(0, 150); // set the fill colour to black with transparency
    rect(mouseX, mouseY, random(6), random(6));
  }


  // save your drawing when you press keyboard 's'
  if (keyPressed == true && key=='s') {
    saveFrame("yourName.jpg");
  }

  // erase your drawing when you press keyboard 'r'
  if (keyPressed == true && key == 'r') {
    background(255);
  }
}
```
5. show them things they can change
6. work through the different sections of the code

end by emphasising
- algorithms
- variables
- debugging
- correct syntax
  - arguments
  