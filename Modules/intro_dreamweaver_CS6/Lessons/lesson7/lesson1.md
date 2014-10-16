# Lesson Template

## Lesson Title

## Lesson number *x* of *y*

## Lesson objective

## Lesson description

In this lesson we are going to do some further work with the styling of the page content using CSS.

Before we begin though just a quick reminder on the difference between content and presentation.  Content is the text or images or other media objects you put into a page.  Presentation refers to how that content is styled and presented.  This could be colour, size or layout.  Ultimately though presentation should not alter content in any way.

CSS allows you to separate content from presentation so that in working with the presentation of the content it won't affect the content at all.

HTML uses tags largely as containers for content.  The default presentation of content contained within a tag you will have probably seen by now is fairly boring.  CSS can therefore start by applying different formatting rules to all instances of that tag on your page.  You can also create other rules with unique names and apply those selectively in a page.

This is a very brief introduction to CSS and I would recommend taking further courses at [Codecademy](http://codecademy.com) using their web design track in order to understand a little bit more about how CSS functions.

In this lesson I am therefore going to dive into how Dreamweaver specifically works with CSS and HTML.  You will need a basic page with some content such as text in paragraphs, images, headings and lists in order to experiment with these tools. This experimentation is something I encourage greatly in order to get as much as possible out of this.

### Setting CSS preferences

Go to Dreamweaver > Preferences and go to the CSS styles panel.  Take off the ticks from all of the shorthand options as this can be a bit confusing to someone starting with CSS.  In answer to 'when double-clicking in CSS panel' I would suggest 'edit using code view' as eventually you may need to be working directly with CSS files and it would be good to get used to the full code view straight away.

### The CSS Panel and setting up a new page with CSS

You will still be working with the CSS panel.  It shows a link to the CSS file attached to your page and the current selectors (at first a list of tags you are working with) and the selector properties.

If you have been following my previous lessons by now you will have a link to a CSS file.  To add a new page and link it to the CSS file you have created already go to File > New and select an HTML page.  Before you click create click the link icon above the attach CSS file box and select the CSS file you have already created.  Save the page and the file should be attached in the `<head> </head>` section of the page.  It will also have the properties you have already chosen applied to that page.

### Adding properties to a new tag

Let's create a new style rule for a heading tag.  Firstly in your page type a heading text and then use Format > Paragraph Format > Heading 1 to change the text into a heading.  This gives us an example piece of text which we can see change when we apply a new set of properties to that tag through the CSS Panel.

In the CSS Panel click on the icon at the bottom which says New CSS Rule.  Under Selector Type choose Tag (redefines an element) and make sure the rule is going to be defined in your CSS file.  You will then be taken to the CSS rule definition dialogue box.  Choose some settings (now is a very good time to experiment!) and click OK.  Your chosen settings will now be applied.

### Editing CSS properties

Once you have setup some properties for the H1 tag you can now edit them using the CSS panel.  You can choose to delete a property, edit a property value directly in the panel or double-click it to edit it either in the CSS file or in the dialogue box.

### Div and Span

### Class and ID
