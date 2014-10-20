# Understanding how to use `<section>` and `<div>` tags

## Lesson number *3* of *5*

## Lesson objective

In this lesson pupils will start to explore some more powerful tags such as `<div>` and `<section>` and start looking at how using different classes can control what tags can do.  Pupils will also start to identify `<div>` tags with a class name which can be used within CSS.

## Lesson description

In the previous lesson you downloaded and setup a Bootstrap template.  You also started to work with some of the more basic tags such as `<h2> </h2>` and `<p> </p>` in order to put in your own content.

**q1: What did the `<h2> </h2>` tag with the content inside it?**
**q2: What did the `<p> </p>` tag with the content inside it?**

In today's lesson you will start to work with some of the more powerful tags used in TML5 pages and bootstrap templates so that you can really start to control what you do with your webpage.

The tags you will be working with are `<section> </section>` and `<div> </div>`.  Both these tags are used to identify sections of a webpage. The `<div> </div>` tags are used to group together elements and are generally used inside a `<section> </section>` tag.

### Activity 1

1. Get your webpage open in the development environment you are using
2. Load the page in a browser so that you are ready to start testing
3. We are now going to add a new section after our last section but before our footer
4. The easiest way to do this is firstly find the footer - search the HTML for `<!-- footer -->` and above it you should see an empty line.
5. Add in some comments in that empty line (feel free to change content but not tags just yet)
```html
<!-- new section -->

<!-- /new section -->
```
6. In between the comments you have just added add the following tags
```html
<section>

</section>
```
7. In between the section tags add four nested `<div>` tags
```html
<div>
	<div>
		<div>
			<div>
			
			</div>
		</div>
	</div>
</div>
```
Remember that nesting tags is kind of like nesting them like the layers of an onion.  I tend to indent them like the above so that I can see which opening and closing tags match.
8. In between the final `<div>` tags add ...
```html
<h2>This is a new section</h2>
<p>This is the first paragraph of the new section</p>
```
9. Save your page if you haven't already been doing so and then open it or refresh the browser.

**q3: Do you notice the new section appear in the web browser? Does it look the same as the other sections?**

### Activity 2

As you can see the text and new section lacks any of the styling of the other sections.  This is because the HTML tags have not been linked to the style rules contained in a CSS file.

A CSS file contains style rules which can be applied to many different webpages.  The HTML page gets its style rules from the CSS document and therefore if you wish to change the style you need to change the rules in the CSS document.

The two CSS documents you will be working with eventually are `bootstrap.css` and `grayscale.css` but for now we will simply attach the style rules by adding a class attribute and classnames.

1. Start off by editing the first `<section>` tag to look like this.  It might be a good idea to save and refresh after adding each classname. 
```html
<section class="container content-section text-center">
```
2. Then add the following classnames to the opening `<div>` tags
```html
        <div class="imagebg-section">
            <div class="container">
                <div class ="row">
                	<div class="col-lg-8 col-lg-offset-2">
```
3. Save and refresh your page now - you should see your new section has taken on some styles similar to the other sections on the page!

Extra: if you have some time an interesting to do is try changing the numbers in
```html
<div class="col-lg-8 col-lg-offset-2">
```
using any number from 1 to 12.  Each time you change it save the page, refresh the browser and also change the size of the browser window.

### Summary:
In today's lesson you have started to work with `<section> </section>` and `<div> </div>` tags and have learnt how to create a new section and add some simple content.  You have also seen how adding classnames from CSS change the style of the tags and what appears in the browser.

In the next lesson you will start to change the CSS rules so that you are able to really change the look and layout of your webpage.