# Setting up a navigation toolbar and Finish

## Lesson number *7* of *7*

## Lesson objective

In this lesson pupils will link the navigation toolbar to the different sections of the page and then complete any outstanding activities.

## Lesson description

In the previous lesson you finished some work with images and looked at some methods for editing the CSS in order to control the look of the page.  We will now work through how to link the navigation toolbar at the top to the `<div>` tags in the main webpage.

### Activity 1

Let's load the index.html page you have been using.  Unless you want to change the colours of any links or buttons on the page we will just be working with the html.

The first section of HTML we are working with is ...
```html
    <nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse">
                    <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="#page-top">
                    <i class="fa fa-play-circle"></i>  <span class="light">Webpage</span> Title
                </a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
                <ul class="nav navbar-nav">
                    <!-- Hidden li included to remove active class from about link when scrolled up past about section -->
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li class="page-scroll">
                        <a href="#about">About</a>
                    </li>
                    <li class="page-scroll">
                        <a href="#section_use">Use of sections</a>
                    </li>
                    <li class="page-scroll">
                        <a href="#section_customise">Customising sections</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>
```
HTML 5 uses a `<nav>` tag to identify a navigation section in a webpage.  The `<nav>` has a number of classes applied to it.  I suggest going and seeing if you can find these class selectors in the CSS and see what they are doing.  If you wish to change any features add those selectors to the grayscale.css and edit them accordingly.

Bootstrap also uses buttons and some associated classes in various places.  There are some examples of buttons further on in the index.html file.

You will then see an `<i>` tag with two classes of fa and fa-play-circle.  This refers to [Font-Awesome](http://fortawesome.github.io/Font-Awesome/) which is a CSS and icon toolkit for putting simple scaleable icons into a page.  Take a look at the link and see if you can change an icon or add a new one in.

Finally we get to where we are going.  Wrapped inside the next `<div>` tag is a `<ul>` element with a number of `<li>` elements.  An unordered list and its list items is a great way to create simple navigational items as each list item is styled as a navigational button using CSS.

These list items can therefore contain a link using an `<a>` tag to another webpage in the website or if you are using one webpage (like we are doing now) you can also link to a section in the webpage.

Taking a look at one of the lits items we see that you have an `<a>` tag with an href attribute beginning with a # and a unique name.
```html
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
```
This unique name is a CSS ID.  If you look further down the index.html page you will see one `<div>` tag with that CSS ID.

How do you use this?  In the final exercise you will identify the ID names for each of the sections, update them and then change the links in the list items in the nav area.

## Activity 2

1.  Identify all of the sections you are using in your webpage.  The easiest way to identify them is find the `<div>` tags with an id attribute.
2.  Change the ID attribute to suit the content in that section.  For example
```html
    <section id="about_cheese" class="container content-section text-center">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2">
                <h2>I Love Cheese!</h2>
                <p>Wallace and Gromit are more my heroes!</p>
            </div>
        </div>
    </section>
```
3.  Go back to the `<nav>` area at the top and edit a `<li> </li>` to match.  For example
```html
                    <li class="page-scroll">
                        <a href="#about_cheese">About Cheese!</a>
                    </li>
```
4.  Save your work and reload it in the browser.  If it has all worked fine you should have a button at the top which links to a section in the webpage.
5.  Update the other links now.

## Finishing off

Through the last seven lessons I have taken you through some of the basics of working with the HTML framework Bootstrap.  I have only touched on the surface of what you can do with this very powerful tool.  There are other frameworks out there which are competitors to Bootstrap but bootstrap is regarded as one of the most capable and is now one of the most used.

If you don't go any further with Bootstrap that's a pity but if you do it's an invaluable skill to have.  I would suggest if you are interested in pushing further with bootstrap read the [documentation](http://getbootstrap.com), start learning Javascript and even a bit of jquery.

Good luck!