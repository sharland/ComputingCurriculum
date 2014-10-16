# Lesson Template

## Lesson Title

## Lesson number *x* of *y*

## Lesson objective

In this lesson we will look at a range of methods for working with images and other multimedia within a web page or site.

## Lesson description

Learning how to work with images is vital for making your site stand out from the crowd.  Images can obviously make a site but they can also break it as well if you approach them in the wrong way.

### Adding images

Dreamweaver allows you to insert images either from your hard drive or from images stored on your defined local site.

In Design view choose a place on the page to insert an image and choose Insert > Image from the menu or use the Insert panel to select an image.  You will be asked to locate the image source (where you have saved it) and provide an alt text attribute for the image.  Alt text is very important as someone with visual impairment using the web would use what is called a screen reader to read through the text on a screen.  Obviously as a screen reader will not be able to 'read' an image it would then read the alt text attribute of that image.  So if you have a picture of a rugby match taking place the alt text owuld say something like "Image of a recent rugby game between the Springboks and England".

If your image was saved outside your defined site you will be asked if you want to copy the file into your site.  I suggest you do this.

The resulting HTML should look something like the following.  You can also obviously use HTML to insert an image directly.
```html
<p><img src="images/IMG_9313.JPG" width="640" height="640" alt="Image of the front of a springbok jersey"></p>
```

All images you have used on your site will be added to the Assets panel.  You can also insert images directly from there as well.

You can also insert image placeholders if you know you want an image but do not know what you want to put in.  Go to Insert > Image Objects > Image Placeholder and follow the instructions to put in an image size and name.  Once you decide to replace it with an image double-click the placeholder and choose an image source.

When you have selected an image there are a number of options you can control within the property box at the bottom including a button which takes the image into Photoshop for further editing.  You can also directly crop or resize an image within Dreamweaver.

### Optimising Images

Be careful about using Dreamweaver to resize images as the full image size is still loaded and having too many full resolution images being loaded by your page will slow down how the page loads.

Dreamweaver does provide some tools to help ensure that your images are the best they can be for the performance of your site.  Go to Modify > Image > Optimize and follow the instructions and options here to tweak your images format and other settings.

### Adding a background image

Go to Modify > Page Properties in the menu and select an image in the Appearance (CSS) category.

If the image is quite small you will want to choose how it will repeat.
*  no-repeat places the image in the top left corner and doesn't repeat it at all
*  repeat fills the page with the repeated image
*  repeat-x repeats the image across the top of the page
*  repeat-y fills the image across the left hand side of the page

Unfortunately Dreamweaver doesn't give you a direct option to set the image not to scroll with the page.  You will have noticed some website doing this when you scroll down the page but the background image remains fixed.

To change this add the line `background-attachment:fixed;` to the body CSS selector at the top of the page like this:
```css
body {
	background-image: url(images/IMG_9334.JPG);
	background-repeat: no-repeat;
	background-attachment:fixed;
}
```
You might want to also move this CSS selector into an external style sheet if you wish to apply this setting to a number of pages.

### Adding a favicon

A favicon i s auseful little touch for webpages.  These are the little icons which appear next to the title of a webpage in the tab of a browser and next to the title when you favourite or bookmark the page.

You will need to find or create a favicon before you can add it to your page.  Try the favicon creator at [http://tools.dynamicdrive.com](http://tools.dynamicdrive.com).

Your created icon should be saved as favicon.ico and I suggest saving it into your images folder.  Add it by going to Insert > HTML > Head Tags > Link.  Select the icon file and in the Rel text box type **shortcut icon**.  After you save and update your site you should see the favicon in place.

### Adding Flash files

To add an exported Flash file (not in the original .fla format) go to the point you wish to insert it (in Design view) and got o Insert > Media > SWF or Insert > Media > Shockwave depending on what file type you are inserting.  Enter alt text and the flash object will be inserted.  You can play the animation in Live view.

You can also insert Flash vide (.flv files) through Insert > Media > FLV.  Tos tart off you should probably choose Progressive Video Download as Streaming Video requires extra software on the server.

A few more settings need to be adjusted including the Skin which is the type of video controller and the width and height of the video.  You can detect the width and height automatically.  The video can also be set to play automatically once someone arrives at the page.

### Adding other media

All other media such as Quicktime video is handled by Dreamweaver as plugin media.  Insert it through Insert > Media > Plugin and choose the file source.


