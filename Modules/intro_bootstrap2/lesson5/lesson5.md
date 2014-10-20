# Working with the images and associated CSS

## Lesson number *5* of *7*

## Lesson objective

In this lesson you are going to do some work on the images within the site through `<img>` tags and CSS styles which control how an image works within a page.

## Lesson description

In the previous lesson you looked at various ways of editing the CSS selectors and rules in order to control how a page is formatted and styled.

You can do a lot with CSS and its formatting options but sometimes one needs images in order to improve how a page looks.  CSS can be used to control what an image does in a webpage and what it looks like.

### Activity 1

Load a picture heavy webpage such as [The Guardian Pictures](http://www.theguardian.com/inpictures) and right-click on an image and select 'inspect element'.

What do you see come up in the HTML?
Can you change a setting or style related to that image in the HTML and see what happens in the webpage?
Could you replace the image? How would you do that? (Think about the source)

### Activity 2

Let's now identify a couple of images we can use in your web-page.  You will need:

1.  At least images which can be inserted into your webpage
2.  At least two images which can be used as a background for the sections in the webpage

*Finding images to insert*

The temptation when finding images for a project is to just go to Google and search for a great image.  However this is not a good thing as although someones photograph might appear on a couple of websites this does not mean they want to have their photograph copied.  These photos therefore have various rights attached to them which largely belong to the person or company which ones that picture.

You can use images which fall under what is known as a Creative Commons license.  Creative Commons is a way of licensing digital products so that others can use them without falling foul of copyright.  Read the wiki link I have attached above.

A great site for finding Creative Commons licensed images is [FlickrCC](http://flickrcc.bluemountains.net) which shows images from flickr.com tagged as Creative Commons.

If you use an image from the site you will need to show on your website the original link to that image.

Therefore for this task I suggest that you now find the images requested which fit the content you are using for your webpage.  Save these images as full size images wherever possible into the same folder as your webpage.  I have also included an example image in the lesson folder.

### Activity 3

Let's now insert these images into the webpage which you are building.  Make sure it is loaded in your development environment.  Identify a `<section>` you are going to use and take a look at an example of how I have inserted an image below.

```html
<!-- Blank with image -->
    <section id="blank_image" class="content-section text-center">
        <div class="imagebg-section">
            <div class="container">
                <div class ="row">
                	<div class="col-lg-8 col-lg-offset-2">
                    	<h2>Raspberry PI/h2>
                    	<p>This is the best computer in the world</p>
                    	<img src="raspberrypi.jpg" alt="the Raspberry PI">
                	</div>
                </div>
            </div>
        </div>
    </section>
<!-- /blank with image -->
```

The `<img>` tag is a self-closing tag and I have used one attribute called src to describe the location of the image file to be used in the tag.

Save your page and load it in a browser.

What happened?  You have may noticed if you used my image that the image has some issues.

### Activity 4

Let's deal with some of those issues.  In the code examples below I will focus on the `<img>` tag but it is still the same tag in the activity 3 section above.

As your image you inserted may have had some size issues we can control the size through an additional attribute in the image.

```
<img src="raspberrypi.jpg" alt="The Raspberry Pi" width="200">
```

Using the width attribute is a great way to control the size of an image.  Unless my original images are way too big (1mb and over) I tend to leave them full size and use a width tag to control how big they should be.  You could obviously use a height attribute instead.  You can use width and height together but if you get the sizing wrong your image will look strange.

### Activity 5

You can use CSS to control certain aspects of the styling of your image.  Open grayscale.css.

At the bottom of grayscale.css add the following css selector and rules:

```css
.img-rounded {
  border-radius: 6px;
}
.img-thumbnail {
  display: inline-block;
  max-width: 100%;
  height: auto;
  padding: 4px;
  line-height: 1.428571429;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  -webkit-transition: all .2s ease-in-out;
          transition: all .2s ease-in-out;
}
.img-circle {
  border-radius: 50%;
}
```
Go back to your index.html file and the `<img>` tag you inserted and add a class like this:
```html
<img src="raspberrypi.jpg" class="img-rounded" alt="The Raspberry Pi" width="200">
```
Save your page and load it in the browser.  Once you have seen what the class does try the other two.  Once you have tried those two classes see what you can change in the CSS rules and how it affects the final image.

### Summary

In this lesson you have covered quite a bit on working with images including finding them, inserting them and styling them.

In the next lesson you are going to look at changing the background of the sections and doing some colouring of the site.
