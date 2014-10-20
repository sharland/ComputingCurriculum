# Working with the CSS to make your site look better

## Lesson number *4* of *7*

## Lesson objective

In this lesson pupils will look at how they can start to modify the CSS to control how the tags and associated content is displayed in the web browser. As part of this pupils will work with hexadecimal colours.

## Lesson description


In the previous lesson you managed to insert a new section within the page using the following structure and then added some class names to the section.  You hopefully also added some content to the tags.

In this lesson you are going to look at editing the CSS files which the HTML is linked so that you can change the look and possibly even the layout of the HTML.

**First some bits about CSS**

CSS stands for 'Cascading Style Sheet'.  It is a separate file to an HTML page and it contains sets of style rules for a webpage.

So for example a CSS file called `stylesheet.css` might contain something which looks like this with four properties and their values ...

```css
p 	{
	background-color:#00FF00;
	font-family:Arial;
	font-size:xx-large;
	color:#0000FF;
}
```
In a webpage you would attach your HTML file to the CSS file using a tag like this in your `<head> ... </head>` area.
```html
<link rel="stylesheet" type="text/css" href="stylesheet.css" />
```
This will link the HTML file to the CSS and the HTML file which might contain this ...
```html
<body>
	<h1>This is a heading</h1>
	<p>This is a paragraph</p>
</body>
```
will display the paragraph with a background colour of green, a font of Arial, a large font size and the text itself will be blue.

### Activity 1

1. Try this now - in the lesson 4 folder there is a folder called `very simple CSS example`.  Open it and you will find an HTML file and a CSS file.  Open the HTML file in your editor and you will see I have deliberately misspelled something in the `<link>` tag.  Fix it and save the file and load it in your browser and you should see the content in the `<p>` tag behave slightly differently.
2. Once you have done that open the CSS file and take a look at the rules I have written for the `<p>` tag.  Can you change them?  The following links might help you:
    - [Choose a hexadecimal colour](http://www.colorpicker.com)
    - [List of CSS properties](http://www.w3schools.com/cssref/)
3. To really see if you can push the CSS further can you write another set of CSS rules in the CSS file for the `<h1>` tag?

### Activity 2

Another easy way to understand what CSS does for a webpage is to actually turn it off for a pre-existing webpage.

You can do this with Internet Explorer, Chrome, Firefox and Safari.  For each browser find out using a search engine how to 'inspect an element'.

Once you have found out how to do that load [http://theguardian.com](http://theguardian.com) and inspect element.  You should see the html for that page appear in a window at the bottom of the screen.

Look for the line beginning `<head>`.  There might be an arrow next to it which if you drop it down will show you all the content inside the `<head>` tag.

Look for a line such as the following, select it and delete it.
```html
<link rel="stylesheet" type="text/css" href="http://static.guim.co.uk/static/31e1b875df396ca28a4f1f304093348ff68735ab/common/styles/network-front-grid.css" media="all">
``` 
What happens to the page?  Try deleting some of the other stylesheet link tags as well.  Refresh the page to bring the style sheet tags.

### Activity 3

Open the webpage you were working on last week and open both the index.html and the grayscale.css file.  We are going to start working with this one just to change how the webpage looks.

A good thing to do before you continue is save a copy of grayscale.css as grayscaleBackup.css in case you need to restore anything.

We will start by working inside the grayscale.css file as it is loaded after bootstrap.css and therefore takes precedence.  We are going to start by making a couple of interesting changes which might produce a result which doesn't necessarily work but which might give you some results.  In grayscale.css look for the following selectors, properties and values and make the change selected.  After each change save the CSS and refresh it in your browser:

*1. Look for*

```css
body {
    width: 100%;
    height: 100%;
    font-family: Lora,"Helvetica Neue",Helvetica,Arial,sans-serif;
    color: #fff;
    background-color: #000;
}
```
*1. Change to:*
```css
body {
    width: 100%;
    height: 100%;
    font-family: Arial,sans-serif;
    color: #00ff00;
    background-color: #ffff00;
}
```
Use the hexadecimal colour picker link above to try out some different colours.  What happened once you made the changes?

*2 Look for*
```css
h1,
h2,
h3,
h4,
h5,
h6 {
    margin: 0 0 35px;
    text-transform: uppercase;
    font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
    font-weight: 700;
    letter-spacing: 1px;
}
```
*2 Change to*
```css
h1,
h2,
h3,
h4,
h5,
h6 {
    margin: 0 0 35px;
    text-transform: capitilise;
    font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
    font-weight: 500;
    letter-spacing: 10px;
}
```
What happened once you made the changes?

*3 Look for*

Lastly a simple one
```css
a:hover,
a:focus {
    text-decoration: none;
    color: #176e61;
}
```

*3 Change to*
```css
a:hover,
a:focus {
    text-decoration: underline;
    color: red;
}
```
What did that do when you moved a mouse over a hyperlink?

### Extension

If you have managed to finish the above tasks quite quickly than start to look through the other CSS rules and see what you can edit.  Always remember to save after each edit and to undo if you did something wrong.  Test as well after each edit.

### Summary

We covered quite a bit in today's lesson.  We looked at the importance of CSS in styling a webpage through a simple example and then breaking the website of a major newspaper!  We also started to edit the CSS of our own site to see what we could do with it.

In the next lesson we will learn how to add our own new selectors and give them some properties and values and then try and finish off our site.


