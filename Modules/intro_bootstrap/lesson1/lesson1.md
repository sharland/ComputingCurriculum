# Building and testing a simple webpage

## Lesson number *1* of *7*

## Lesson objective

In this lesson pupils will assess different sorts of development environments and then open their own school provided development environment.  Pupils will then use the software to build and test a very simple webpage using a basic HTML structure.

## Lesson description

### Activity 1: seeing how webpages display content

Let's open your favourite website.  Make sure it's one which is allowed on the school network.  For myself it will probably be [http://theguardian.com](http://theguardian.com).  These sites are fantastic examples of modern web-based technology.

**q1: When you access a webpage what is actually being downloaded to your computer?**

To answer this question let's take a look at an example webpage which you have open on your screen.  Use the one given above or any other.

Find an area of the web page, right click to get a shortcut menu and find an option to 'view source' (various browsers will have different links - I suggest using Chrome).

You will now see a page containing the HTML for that web page.  This is what is being downloaded to your browser and what your browser is interpreting to display as a webpage.

### Activity 2: Changing some of the HTML in a webpage

For this activity you will need a modern web browser such as Chrome.

1. Go to [The Guardian](http://www.theguardian.com)
2. Right click on a heading on a news article and select *inspect element*
3. A section of HTML will apear at the bottom of the screen.  Locate the heading text inside the HTML so if the heading was 'Actual Spaghetti Tree discovered' then find that same text in the HTML
4. Click on that text, delete it and replace it with your own text.  When you hit enter the text will update on the website.
5. Try some other changes.  When you have finished reload the page.

**q2: How many lines of HTML are there?**

You will have seen from the page source of your own website and editing the Guardian that websites today contain a lot of HTML.

**q3: How was this created?**

If it's any of the popular websites you use today one person did nto set and write all of those thousands of lines of code.  Most websites today would have been built using a variety of methods and often by teams of pupils.

**q4: How are we going to build a website?**

We are going to be looking in the next couple of lessons at how to use one method of quickly setting up and editing a professional looking website.

### Activity 3: Identify your development environment

An Interactive Development Environment is software used to develop software.  As modern websites can use simple programming they are sometimes viewed as 'web apps'.  Developing websites nowadays can therefore be quite a complex task and sometimes more advanced tools are required.

To begin with we are going to create a simple webpage using a very simple piece of software called Notepad.  Follow the instructions below:

1. Create a folder in your own area on the school network called `simple_website`
2. Open Notepad on your computer
3. Before you write anything save the file into the folder `simple_website` as `index.htm` and leave Notepad open
4. Go to that folder and double-click the file.  It should load in a browser on your computer but it will not show anything
5. Leave the file open in the browser - once you have made some changes in Notepad and saved those changes you will only need to refresh the browser to see those changes
6.  Let's add some simple tags and content in order to make a basic webpage
  * Write `<!DOCTYPE html>` into the first line.  This will tell the browser that you are using the latest version of HTML which is 5.
  * On the next two lines add the following which will tell the browser to expect an HTML document
  ```html
  <html>
  
  </html>
  ```
  * Remember that everything we are going to continue to add goes between the `<html></html>` tags.  Think of them like an onion skin wrapping content inside.  Next add the following code inside your `<html></html` tags.
  ```html
  <head>
  
  </head>
  <body>
  
  </body>
  ```
  This will create the head section for storing meta data about the site and the body for displaying the content.  Meta data is data about the webpage itself such as its title and keywords which a search engine will use.
  * Try save your work now and refresh it in the browser.  It is a very basic webpage structure but there will still be nothing inside the browser.
  * As there is still no content let's add a little bit.  Inside the `<head></head>` tags add the following tag and content.  You are allowed to change the text in between the tags.
  ```html
  <title>Welcome to my website</title>
  ```
  * The next content is going to go inside the `<body></body>` tags.  This is going to be the content for the webpage itself.  Feel free to change any content in between the tags.
  ```html
  <nav>
  	<p>My Menu</p>
  	<ul>
  		<li><a href="aboutme">About Me</a></li>
  		<li><a href="myinterests">My Interests</a></li>
  	</ul>
  </nav>
  <section id="aboutme">
  	<h1>About me</h1>
  	<p>This paragraph is all about me - feel free to change</p>
  </section>
  <section id="myinterests">
  	<h1>My Interests</h1>
  	<p>These are my interests - feel free to change</p>
  </section>
  <footer>
  	<p>Site built by me</p>
  </footer>
```
  * Now try and save and refresh the browser - you should see a very basic webpage appear.
  * If you would like to and are familiar with extra HTML tags you may carry on adding to the basic webpage if you like.

### Summary

Creating this very simple webpage probably took a reasonable amount of effort (unless you copied and pasted!).  This however is only one page which you have built which contains no styling and no images.  So why did we do this?

1. Before the next lesson it has helped to remind you about the basic structure of a simple webpage which is what we covered above.
2. You will have seen that building a webpage is not that easy and that in order to produce awesome websites like [this](http://roxannekoranda.com) takes time, effort, knowledge and skill.
3.  You will have also learnt how to take a look at the code from other websites.  This can be a great way to see how other websites are built.

 
