# pyApolloPhotosDownloader (Flickr downloader)

## Introduction

This is a Python 3.x script that extracts a list of direct links to high-resolution photos from [NASA's Apollo mission Flickr photostream](https://www.flickr.com/photos/projectapolloarchive). You then give that list to wget and download it all.

The moment I saw they posted literally over 9000 photos, I had to have them. Trying numerous "Flickr downloaders" was disappointing to say the least, so I wrote my own script in like an hour. Decided to publish it, so I refined it a bit and here it is!

## How to use it

You need Python 3.x for any platform. Windows, OS X and Linux should all work. (I tested only on Debian.)

You also need some file downloader that can load up a list of files to download like wget, curl or FDM for Windows.

Download the script and just run it with `python3 pyApolloDL.py`

It creates a file with a list of direct links which you then give to wget like this: `wget -i photolinks.lst`

Wget downloads all photos in the same folder and voila!


### Example

```
$ python3 pyApolloDL.py 
pyApolloPhotosDownloader v0.1 ALPHA - Flickr downloader
Coded by JackFrancisD <jackfd@openmailbox.org>
==========================================================
[!] This software is an early version. No errors are handled, but it does work.
[*] Starting Flickr direct link extraction from https://www.flickr.com/photos/projectapolloarchive
[*] Extracting page count...
[*] 101 pages found.
[*] Getting direct links from page 1...
[*] Getting direct links from page 2...
[*] Getting direct links from page 3...
[*] Getting direct links from page 4...
[*] Getting direct links from page 5...
[*] Getting direct links from page 6...

...

[*] Writing links to 'photolinks.lst'...
[*] Done! Use `wget -i photolinks.lst` to download.
```

Now just use wget or whatever to download the pics.

```
$ wget -i photolinks.lst
```

## Modification

This script can be easily modified to download other photostreams from Flickr.

However, keep in mind that the script only downloads photos in "Original" size from Flickr, and only if the uploader has enabled downloads (the latter has not been tested, to be honest, but I suppose that's the case).

If you've got Python skillz, you can modify the script to download different sizes, and to circumvent disabled downloads, but it'll take you time.

**NOTE:** This script has only been tested with photostreams that span 10+ pages long. `getPageCount()` function relies on those three dots (`...`) between pages at the bottom of the photostream to count the pages properly. If that's missing, you have to modify the function or force it to return a custom, manually entered number of pages.


### Algorithm

The script works like this:

 - Use `urllib` to download the HTML from the `MAIN_URL` variable.
 - Parse the HTML to extract the number of pages from it.
 - Repeat the following loop for each page:
 	- Download the HTML of the page
 	- Parse it to extract direct links to "Original"-sized images
 	- Append links to a global variable `finalLinksList`
 - Once done, write all links to a file whose filename is set by `LINKS_LIST_FILENAME`


## Contribute!

If you give enough of a shit, feel free to submit patches, I'm happy to accept them as I probably won't be improving this script much unless I need it again for something.

I am aware of all the issues (like no error checking and error handling), so don't waste your time submitting issues. If you wanna help, fix them, it's easy as the script is quite simple.

Cheers,
JackFrancisD
