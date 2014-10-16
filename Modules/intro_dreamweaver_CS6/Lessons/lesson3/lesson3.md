# Lesson Template

## Lesson Title

## Lesson number *x* of *y*

## Lesson objective

Look at how to build your first webpage

## Lesson description

In this lesson we are going to look at how to build your first webpage.

### Creating a new page

There are a couple of ways to create a new page (File > New being the most obvious).  When you do you will be given a choice of templates and page types to choose from.  The amount of choice may seem quite overwhelming but if you start with the basics you should have the confidence to eventually work with more complex templates and page types.

You will essentially be given a choice between fixed and fluid page layouts with some additional scripting languages such as PHP available as well.  A fixed page will contain a simple template which will appear the same no matter what size screen you view it on (smart phone or desktop).  A fluid page will contain a template layout which will adjust how it looks depending on the screen resolution of the device being used to view it.  So a site built using a fluid layout will look one way on a desktop but will look slightly different on a phone with different placement of text, images and navigational elements.

### Choosing a doctype

In lesson 1 I suggested that you use the Dreamweaver preferences menu to change the HTML version of new pages to HTML5.  Unless you have a good reason to work in XHTML (the default) I strongly suggest you work in HTML5 as it is becoming the standard for modern dynamic websites.

The doctype is therefore the declaration at the top of the page telling the browser what version of HTML to expect below so that it knows how to 'render' or display it.  The HTML5 doctype looks like this ...
```html
<!DOCTYPE html>
```

### Titling your page

Every page needs a title.  It is what is shown in the browser window at the top and used if your page is bookmarked in a browser.  Set it now by using the title box in the editing menu or by adding to the `<head> </head>` section:
```html
<title>An example page title!</title>
```

### Adding text to your page

This depends very much now on which view you have chosen.  In design view you will be able to simply click on the page and start writing text.  If you then click on code view you will see how Dreamweaver has automatically created the HTML for you.  I suppose this way works fine but once can get a bit lazy with the layout and structure of your page.

**Warning**

At this point you may obviously be tempted to start formatting your text using the available options.  If you do so this will create a type of HTML styling known as inline styles.  This is OK for single page small websites but if you want to start working at a higher level already ignore all of the built in formatting options and hold on until you can start to apply basic CSS rules.  I promise you it will be worth it!

### Creating links

Webpages without hyperlinks are not very useful.  Think about what wikipedia would be like if there were no links in articles to other articles.

To insert a hyperlink create the text on the page which will hold a link.  Using the property inspector you can then setup either an internal link to a file in your local site or an external link to another website.

To setup an internal link use the point to file button in the property inspector or the browse for file button to find the file you wish to link to.

To setup an external link simply type the full URL of the website (including the http:// at the beginning of the address - some browsers don't display this anymore but it is still there) into the link property box such as **http://www.bbc.co.uk**.

To add a link using HTML you will need to swap to the code view (or split view so you can see how your changes look straight away) and inside the `<body> </body>` tags add:
```html
<a href="http:/www.bbc.co.uk">Click here to go to the BBC</a>
```

### Inserting images

Inserting images will obviously improve the visual appeal of your website.  To do this one way within Dreamweaver you could use the Insert panel and choose the Image option.  This will allow you to select the image and configure a few options for it.  If the image is not inside your defined dreamweaver site Dreamweaver will automatically copy the image to the default images site you setup earlier.  In between the `<body> </body>` tags add:
```html
<img src="../images/exampleImage.jpg" alt="An example image" height="500" width="300">
```
The alt attribute is important as it provides a description for the image which can be used by those with visual impairment surfing the web with screen readers.

The image height and width can also be controlled through attributes within the img tag.  The measurements are in pixels.  It is not a good idea to use the height and width attributes to scale a very large image down to a very small image as the webpage has to load the very large image.  This means that if you are resizing a number of images the web page will take a very long time to load.

### Saving your page

To save your page click on File > Save or Ctrl-S or cmd-S.  It is important that when you save your page you ensure that the file has an extension of .htm or .html.

### Previewing in a browser

When you are editing a page in Dreamweaver you obviously want to be able to see how it looks in a range of browsers.  The reason why you need to test in multiple browsers is that not everyone uses the same browser and different browsers may render the pages in slightly different ways.

A minimum range of browsers to test in would be:
* Internet Explorer
* Chrome
* Firefox
* Safari

To preview your work directly within Dreamweaver use the Live view which uses the same rendering approach as Chrome and Safari.

To preview your work directly in a web browser save it firstly and then use File > Preview in Browser which will show you a list of browsers you have installed on your system to choose from.

What I often do is once I have a page loaded in a browser I simply leave it open and whenever I make a change in Dreamweaver I save it, go back to the browser and refresh.

The list of browsers can also be managed in your Preferences.

### Previewing using different screen sizes

Many users may also want to view your webpage on a mobile phone or on a tablet and this means you will need to test your browser using different resolutions or even on those devices as well.  If you are are building a responsive site it is obviously a god idea to do this in any case and Dreamweaver has some tools to help you.

To change viewport size within the live view in Dreamweaver there is a multiscreen preview button.  Use this to change the viewport size you wish to test.  You can also choose the orientation as well.

You can also adjust the preview sizes available, for instance if you are testing for a non-standard device, in Dreamweaver preferences.

Adobe also uses a service called BrowserLab to help with testing webpages in multiple browsers.

### Setting up page properties

At this point you may wish to delve into the properties of your page.  These are some quite important settings which can affect the appearance of your page and how it is handled by search engines.

To set your page properties go to Modify > Page properties.

The first few categories control the Appearance of the page through basic CSS and HTML.  This is fine if you want to do some quick modifications to your appearance but as we will be delving into full external CSS files in a later lesson I would again suggest holding off from using these.  Take a look instead at the Title/Encoding section as this is where you can set your title for the page but also, more importantly, control the document type if you wish to use something else other than HTML5.

### Setting up Meta tags

Meta tags are important elements to add to a page as they help search engines understand what content is within your page.  You can add keywords, text descriptions of your page and links to external style sheets.

Refresh is an interesting meta tag to add as it can force the page to refresh which may be useful if you want to force the page to display new content which is being pulled from other sources.  You could also use it to build a splash page which automatically transitions to another page after a set amount of time.


