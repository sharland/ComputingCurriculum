# Working with more Images and CSS

## Lesson number *6* of *7*

## Lesson objective

In this lesson pupils will continue with some further CSS editing with background images as well as work with some colours.

## Lesson description

In the previous lesson you started to work with the images within the page and how they appeared.  Aspects of their appearance are controlled in CSS.  We still however have the same rather dull background images and almost black page!

### Activity 1

*Find some more images*

Using the same skills from the previous lesson, find two photos from [here](http://flickrcc.bluemountains.net) to use as background images for some of your sections.

These images need to be of sufficient size to be used. The current background image for the main splash at the top is 1500 pixels by 1125.  The image used for the other sections is 1850 by 400 pixels.  You can use pictures of different sizes but you may get some interesting results.

Once you have found the two images you will need to save them into your images folder within your webpage folder.  You will see that the two current images are there - leave them for now.

### Activity 2

Open the grayscale.css file in your website editor and look for the following two css selectors.

```css
.intro {
    display: table;
    width: 100%;
    height: auto;
    padding: 100px 0;
    text-align: center;
    color: #fff;
    background: url(../img/intro-bg.jpg) no-repeat bottom center scroll;
    background-color: #000;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    background-size: cover;
    -o-background-size: cover;
}
```
and
```css
.imagebg-section {
    width: 100%;
    padding: 100px 0;
    color: #fff;
    background: url(../img/downloads-bg.jpg) no-repeat center center scroll;
    background-color: #000;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    background-size: cover;
    -o-background-size: cover;
}
```
Look for the CSS rule in both called `background:` and change the image file names to the ones you have found.  You have to make sure you keep the url path with the dots and the img folder as this refers to the subfolder img containing your files.

Save your grayscale.css file and test it in your browser.  You should see the background images change.

### Activity 2

*Working with colour*

Before we get going there is one important note to make.  In my lesson notes I will use the word 'colour' whereas in CSS 'colour' is spelt the American way 'color'.  You will therefore have to make sure you use 'color' in your CSS.

We will be working with grayscale.css again.  Have it open and look for the following CSS selector and rules.
```css
body {
    width: 100%;
    height: 100%;
    font-family: Lora,"Helvetica Neue",Helvetica,Arial,sans-serif;
    color: #fff;
    background-color: #000;
}
```
```css
    .top-nav-collapse {
        padding: 0;
        background-color: #000;
    }
```
The first CSS selector will target a couple of attributes of the entire web-page.  I would suggest leaving the width and height (although experiment with them by all means to see what results you get.  Change the font-family attribute by all means.  You will need to identify suitable font-families you can use and put them in.  The first font is the one you want absolutely to be used but the ones after that are used if the browser doesn't support the first font.  You lastly finish with a generic family of either serif or sans-serif.

Next try change the font colour which is represented just as `color:#fff`.  At the moment it is written as a shorter hex code but for more fine-tuned colours you may need to use a full hex code such as #3EA9A1 which should give you a nice pale blue.  Use a site like [ColourLovers.com](http://www.colourlovers.com) or [ColorHexa.com](http://www.colorhexa.com) to help you choose your colours.  You can also change the background colour as well.  Think carefully about your colour choices!

The `.top-nav-collapse` selector refers to the menu bar which appears when you scroll down and it turns solid.  At the moment it is black so if you change the background colour attribute you will be able to change the toolbar colour to support your colour theme.

Carry on experimenting with colour options.  If you spot something else in the grayscale.css fil you would like to try and change but you are not sure how to do it I would suggest that you head to google and search for CSS and the name of the attribute you would like to find out about.

### Working with the grayscale.css and bootstrap.css

You may have noticed that all of the CSS work we have been doing so far has been in grayscale.css but that you also have a file called bootstrap.css.  The easiest way to understand the difference between the two is that grayscale.css contains the main customisation for the webpage which sets it apart from other webpages built using bootstrap and bootstrap.css contains the basic layout of the page.  An example of a page built using with no extra customisations and just using boostrap.css can be found [here](http://getbootstrap.com/examples/jumbotron-narrow/).

If you want to edit anything in the bootstrap.css file it is far better to write a set of CSS rules for the same selector in grayscale.css.  As grayscale.css is loaded after bootstrap.css (take a look at the order of css files in index.html).  This means that if a rule from bootstrap.css is loaded it is then superseded by the same rule in grayscale.css.

### Summary

In this lesson you have looked at changing some of the images in the webpage, specifically the ones behind certain sections, using CSS.  You have also looked at changing some of the CSS rules related the colour and general formatting for the page.