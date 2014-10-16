# Lesson Template

## Lesson Title

## Lesson number *x* of *y*

## Lesson objective

In this lesson we will be looking at more advanced techniques for editing text in Dreamweaver.

## Lesson description

In a previous lesson I looked at some basic text editing as part of getting started within Dreamweaver.  In this lesson we will look a little bit more closely at some more advanced editing techniques for text so that you will be a little bit more prepared for working with CSS.  This lesson will not be teaching you the basics of HTML and I will assume you have some basic knowledge.  I would suggest one of the HTML courses from [http://codecademy.com](http://codecademy.com) as a good way to get started with learning HTML.

The first issue to consider when working with text is what view you are working in within Dreamweaver.  In Design view you will be seeing only the text you are writing and not the HTML tags used with the text.  These you will see in Code view (and obviously Split View which shows both Code and Design).

If you begin writing in Code view Dreamweaver does not automatically add tags for you.  A good way to see how tags are generated (and to learn a little bit more about what each tag does) is to use Split view and write your text in the Design side of split view.  This will show you the code view update with the relevant tags.

### Basic editing

Basic editing is fairly simple to get to grips with.  Dreamweaver supports copy and paste for both normal text and copying HTML from one page to another page.  If you copy HML into Design view it will display al of the tags in design view.  This is a nice way to quickly include HTML for a tutorial web page.

You can also use paste special to bring in text from programs like Microsoft Word and control how the formatting is displayed.  You can also drag and drop text easily as well.

Tabs are not supported in HTML but a CSS rule using the **text-indent** property will help.

You can also use paragrap alignment such as left, centre, right and justify.  Later on in this lesson I introduce you to the concept of setting up CSS rules using an external style sheet and this would be a good place to store rules related to paragraph alignment.

### Inserting Headings

HTML supports 6 built in headings using the `<h1> Heading text </h1>` tag (down to `<h6>`) and these are very useful for starting to work with the structure and formatting of your text.  Try insert one now by either putting the container tag for a heading around some text in Code view or by going into Design view, highlighting some text and then using the properties box and the format option to select a heading.

Using headings is a good idea as most CSS targets headings for different styles.  Google also looks at headings when indexing pages so using them effectively is a good idea.

### Applying Text Styles

Up to now I have been mentioning CSS as well as asking you to avoid applying certain formatting options.  If you decide to try using basic formatting directly within each page you write you would end up using a lot of `<font>` tags or embedded CSS to style your page.  This may be useful for more basic scenarios or web pages where you don't ever plan to change the styling.  Putting those styles into an external CSS sheet will enable you to change your styling using the external style sheet and see all pages connected to the external CSS sheet.

Fortunately Dreamweaver helps you get going with the creation of an external CSS style sheet.  If let's say you want to add some colour to a piece of text you can use the Format menu to select Color and then choose a colour.  Once you have chosen it Dreamweaver will ask you a couple of things to help set up your CSS.  Firstly it will ask you for a selector type.  For now I would suggest you use class unless you want this style rule to only be used once in the whole page in which case I would suggest using ID.  Next you will need to supply the name of the CSS selector.  A CSS selector can store a number of separate formatting rules which are applied whenever that CSS selector is used.  Finally choose where you want your CSS rule to be defined and here is where I strongly recommend you choose an external CSS file.  It may seem daunting at first but as you grow in confidence with website design it will make things a lot easier.

Some text styles can be applied directly using tags such as `<strong> ... </strong>` to make things bold.  These are also very useful especially as you can target them using CSS.

I would suggest experimenting now with a demo HTML page with some text in it.  Try as many styles as you can with some dummy text as the best way you will be able to learn is through testing them out.  Always use the same principle though of storing the CSS rules you develop in an external CSS file.

### Inserting line breaks

Just a quick note on a very useful tag for creating a line break.  Sometimes when working with text you may want text on a newline without forcing a space after a paragraph using a `<p>...</p>` tag.  Use a line break `<br />` instead.  This is also useful when working with some languages like PHP.

### Inserting Lists

Lists, both numbered and unordered, may seem like a very plain way of structuring text within your page but with CSS they can be extremely powerful tools.  Although we won't get far with them now eventually you could use lists along with CSS to create fancy navigational toolbars.

To create a list in design view type a list and then use the Format > List menu option to change it into a list.  Change your view to split view and you will see how Dreamweaver sets up the necessary tags like below.

```html
		<ul>
			<li>Lesson 1</li>
			  <ul>
			    <li>nested list item 1</li>
			    <li>nested list item 2</li>
		      </ul>
			<li>Lesson 2</li>
            <li>Lesson 3</li>
		</ul>
```

List properties can be controlled through Format > List > Properties.  You can also nest list items like the example above.  However you might notice that Dreamweaver handles the `<li> ... </li>` tags slightly differently when nesting sub points.  I prefer the structure I've written above.

### Inserting current data and time

Use Insert > Date and the available properties and settings to setup an automatic date and time for your page.

