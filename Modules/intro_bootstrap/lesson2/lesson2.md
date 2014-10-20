# Downloading and setting up Bootstrap

## Lesson number *2* of *7*

## Lesson objective

In this lesson pupils will download a Bootstrap template or use one provided by the school.  They will open it within their web-editing software and then begin by identifying the different parts of the web-page before beginning to edit simple text within the web-page itself. Pupils will also be encouraged to add further content through the use of simple hashtags such as `<p>` and `<h1>` and observe how the CSS styles the content.

## Lesson description

**Introduction and recap of last lesson**

In the last lesson we saw that writing a web-page takes a fair bit of work and that doing it from scratch would take quite a while until you have something usable.

In this lesson we are going to look at how we can use a Bootstrap template in order to speed up how we create a webpage.

A template is preset document containing some of the structure and styling initially required to create a webpage.  The Bootstrap template was originally created at Twitter as a way for developers to quickly create new websites for projects.

**Decide on a topic for your webpage**

Late on in this lesson you will begin to edit your own bootstrap template.  Decide now what your webpage will be about.  A good suggestion would be to make a webpage showing off some of the work you have completed in Computing.

**Examples of Bootstrap templates and sites**

Here are some examples of Bootstrap templates - take a look through them

1. [Freelancer](http://startbootstrap.com/freelancer)
2. [Music-Nation](https://wrapbootstrap.com/theme/music-nation-responsive-dark-template-WB07K727X)
3. [Builder](http://themes.orange-idea.com/?theme=builder)

Here are some examples of sites created using Bootstrap templates

1. [Riser Agency](http://www.riseragency.com)
2. [Redbubble](http://www.redbubble.com)
3. [Lost planet](http://www.lostplanetthegame.com)

For each of the sites you take a look try and change the size of the browser window you are viewing the site with.  What you notice is the site content and layout will change or 'respond' to the changing size of the browser.  This means that the site is known as a 'responsive' website.  It is how developers can quickly build a website for a desktop browser and have that same website viewable on a browser on a mobile phone.

### Activity 1 - Getting setup

So let's grab our first Bootstrap template and get it setup.  I would suggest you go through the following steps to get started:

1. In your own personal area on the school network create a folder called `personal_site`
2. This lesson contains a simplified one-page template in a folder called `bootstrap_template`.  Copy the contents to the folder you have just created.
3. Use the development environment you are using on your computer to either:
  - open the index.html file directly
  - setup a folder or project in order to access and open index.html
4. Use the development environment to open the page in a browser so that you can see what it looks like
5. Your template is now setup and ready to use

**The structure of a Bootstrap HTML5 template**

Make sure you have opened the index.html file in your editor software.  Let's now try and identify certain parts of it.  Below is a very simplified version of the file showing the key parts of the index.html file.  Once you have identified each part we will move onto your first edits.

Most modern websites, including all Bootstrap templates, use the latest version of HTML called HTML5.  This gives website designers a couple of extra nice features.  When you read through the HTML in the index.html file you will occasionally see code which looks like this:
```html
<!-- This is a comment -->
```
This is a comment which has been inserted into the webpage in order to give some further explanation regarding the code.  I have used it both in the example bootstrap file I have given you as well as the code below.

```html
<!-- The DOCTYPE tag informs the browser which version of HTML is being used - in this case version 5 -->
<!DOCTYPE html>
<!-- The HTML tag begins the rest of the HTML document -->
<html>
	<!-- The head contains all head information, in other words information about the page -->
	<head>
		<!-- META elements contain specific information about the page including things such as page information, keywords and author -->
		<meta name="example" content="example">
		<!-- The TITLE contains a short piece of text which will appear in the browser's main toolbar at the top or within the tab toolbar-->
		<title>Page Title</title>
		<!-- The LINK tags contains a link to an external document such as a CSS file which provides formatting styles to the HTML -->
		<link href="example.css" type="text/css">
	</head>
	<!-- The BODY is where the main content for the webpage will appear -->
	<body>
		<!-- NAV is used to define an area for gathering navigation links for a page.  You would use it for the toolbar -->
		<nav>
		
		</nav>
		<!-- Defining a SECTION is a useful way to create an identifiable area within a page.  You would commonly use an id selector to name it and a class selector to apply a style -->
		<section>
		
		</section>
		<!-- A FOOTER is an identifiable end section to the page -->
		<footer>
		
		</footer>
		<!-- Links to javascript and jquery files are usually placed at the end of the body section -->
		<script type="text/javascript" src="example javascript src file"></script>
	</body>
</html>
```
### Activity 2 - quickly design your page

Now that you have a good idea of the structure of your page let's quickly design it.  You have chosen a topic for your page so let's decide on four sections.  Write these up in a text document using a heading for each section and a short description of the content eg:

- Section 1: About me
  * In this section I will write a short piece about myself and include a picture.

### Activity 3 - making your first edits

In the index.html file you have opened find a section with the id of blank_image.  Inside it you will see the following html:

```html
    <section id="blank_image" class="content-section text-center">
        <div class="imagebg-section">
            <div class="container">
                <div class="col-lg-8 col-lg-offset-2">
                    <h2>Blank with image</h2>
                    <p>Add your own text</p>
                </div>
            </div>
        </div>
    </section>
```
1. Change the text in-between `<h2> </h2>` to something related to the topic for your webpage.
2. Change the paragrap text in-between the `<p> </p>` tags to something related to your topic
3. Save the page and load it in a browser

Congratulations - you have now made your first edits to a bootstrap template.

### Activity 4 - continuing to edit your page

By now you will have hopefully seen that outside the `<nav> </nav` and `<footer </footer>` sections in the index.html page you are working with that there are four separate sections.  Using the simple design from earlier start editing the content in the `<h2> </h2>` tags and `<p> </p>` tags in the other four sections.

### Summary

You have now seen that although a Bootstrap template contains a lot of HTML tags and pre-written content it is hopefully fairly easy for you to edit the content and change a webpage using a Bootstrap template to suit yourself.  This also means it's now a lot quicker to setup content for a professional looking website.

You still may have a way to go before creating full professional websites but at least you have started on the path.