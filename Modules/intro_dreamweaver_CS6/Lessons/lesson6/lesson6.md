# Lesson Template

## Lesson Title

## Lesson number *x* of *y*

## Lesson objective

## Lesson description

In this lesson we are going to be looking at how to work with hyperlinks within Dreamweaver.

### Adding a text link

Start by typing some text which will be turned into a link.  There are a number of ways to turn this into a link but first we need to clarify the difference between an internal and external hyperlink.

*  Internal link: This points to a file stored elsewhere in the defined Dreamweaver site
*  External link: This points to a URL of another web page or website

To create a link, whether internal or external highlight the text which you want to turn into a link.  Go to Insert > Hyperlink.  The dialogue box which pops up will show you a couple of options you need to choose.

In the link field either type in a URL such as http://www.bbc.co.uk or use the folder button to select the file you wish to link to.

You can also choose the target for the link.  This defines where the linked page is going to open.  If you ignore it by default the link will open in the same window.  If you would like your links to open in a different window use _blank as the target.  Another useful one is _new which will create a new window but each time you click a link after that in the original page it will open in that same new window which was created.

### Formatting links

Once you have setup a couple of links you will notice that they are the default blue underlined.  To format all links on the page you will need to use CSS to do this.

Have the CSS styles panel open at the side and click the New CSS Style button.  If you want this new format for hyperlinks to apply to all the links on the page the selector type should be Tag however if you only want it to apply to a couple of your links (perhaps you want the links in a navigation bar to be different) then use Class as your selector.

For now we are going to work with Tag as a selector so all hyperlinks will have their formatting changed.  Choose the a tag for hyperlinks and in rule definition choose where you want the rule to be defined which will be either in the same document or preferably in an external style sheet which you might by now have already setup.

Once you click OK you are then taken to the Rule Definition where you can now setup a couple of formatting changes for the a tag.

We are going to start off simple and just change the colour for the link and the font-weight to bold.  Now is the time to experiment and see what you can come up with.

You will notice that on some websites you visit when you move your mouse over a hyperlink but you do not click on it the hyperlink may change in colour or in some other way.  This is called a pseudo selector and can be changed through adding a new CSS rule and this time choosing a compound selector and following the options.

### Adding anchors

Anchors are very useful for linking to a part of a page and not going straight to the top of the page.  To do this you will need to setup the anchor first on your page to allow another page to link to that anchor.

Go to the part of the page you want the named anchor to go and then from the Insert Panel find Named Anchor and click it.  Choose a name for the anchor which will form part of the hyperlink.  You can then use the property box for a piece of highlighted text elsewhere on the page to select that named anchor.

To link to that anchor from another page it is not as easy.  You will have to create a standard link to the page containing the anchor using the dialogue box or through whatever means feels comfortable to you.  Once the link has been created go to the HTML for that page and find the link text.  Add the name of the anchor to the end of the URL in the link after a #.

Before adding anchor:
```
<a href="demoPage.htm">Link to anchor on demo page</a>
```
After adding anchor link:
```
<a href="demoPage.html#namedanchor">Link to anchor on demo page</a>
```

### Adding links to Graphics

The process for doing this is almost exactly the same as creating a link using text.  Select the image and then choose either Insert > Hyperlink or use the property inspector to browse for a file or enter a URL.

### Creating Image Maps

Select the image you want to turn into an image map.

In the property inspector below you will see a Map text box.  Enter a name which only uses letters, numbers or the underscore and then use the drawing tools to draw an area on the image which will become a link.  You will then be given a link box to choose a file or enter a URL for the link.

### Creating Email links

Sometimes you might want to have someone send an email to yourself directly through the site.  I don't recommend this as it is a common way for spammers to find email addresses to use in spam.

If you do want to do it highlight the text you want to change into a mail link and then use the Email Link button from the Insert panel.