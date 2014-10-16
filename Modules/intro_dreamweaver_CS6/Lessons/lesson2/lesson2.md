# Lesson Template

## Lesson Title

## Lesson number *x* of *y*

## Lesson objective

Look at sites management using local and remote

##Lesson description

Dreamweaver is not just about building webpages but about building full websites.  In this lesson we will look at how to setup a local site and a remote site and how to work with both.

When you build a site in dreamweaver you start by creating and testing a local site.  You do not have to wait to complete the site locally though before you can connect to a remote site and start managing how the site looks remotely.  A remote site is simply the webserver you will be storing your website on for others to view.

It is not a good idea to edit your files only on the remote server as if that server is taken offline or hacked you will lose access to your only copy of your work.

### Setting up your local site

A local site folder is known as your 'local root folder'.  I suggest that within that folder you create subfolders for each of the webpages you are going to create and a subfolder each for CSS, JS and other language resources as well as a subfolder for images and other media which will be used on all pages.

### Understanding static versus dynamic sites

A *static* site is one where you build all the webpages locally and then upload them to a remote site.

A *dynamic* site is one where the pages are created based on information drawn from a database.  Many e-commerce sites are dynamic sites and each page is simply created dynamically as soon as someone accesses a product from a list for example.

Dreamweaver can work with content management systems such as Wordpress and Drupal.

### Moving from local to remote

Once you have finished working on the static pages (or even while you are still working on them) for your site you will connect to a remote site and upload your pages to that site.

This site is known as the *remote site* and it should ideally be a copy of what you are working on locally although until you choose to refresh a remote site there may be some discrepancy.

### Creating a site

Go to Site > New Site to setup a new site.  You will need to put in a name of the site and choose a folder for it.  You don't have to create a new blank folder as you can choose a folder you have already created and setup with website assets.  This means if you have been working in another website design software you can transition quite seamlessly to Dreamweaver.

I suggest going to advanced settings and choosing a default images folder and also creating a web address even if you are just going to be working locally. If I'm just working locally I tend to use site addresses such as http://exampleSiteName.local.

### Setting up a remote server

A remote site is the webserver onto which you are going to load your website.  You can setup your remote server details when you setup your site for the first time but for now I would suggest leaving it.  You can use the Manage Sites command under the site menu option to go back and add a remote site (as well as change other settings to do with your site at a later stage.

If you do start working with remote sites the three main operations you will need to become familiar with are Put and Get and Synchronise.  To put a file means to upload it to a webserver.  To get a file means to download it from a webserver.  You will need to be careful about which versions you are putting and getting in case you end up over-writing crucial information.  So always check before you do!

Synchronise means to make sure that the local copy and remote copy match.  This will mean choosing the files you need to synchronise.



