# pyApolloPhotosDownloader (Flickr downloader)

## Introduction

This is a Python 3.x script that extracts a list of direct links to high-resolution photos from [NASA's Apollo mission Flickr photostream](https://www.flickr.com/photos/projectapolloarchive). You then give that list to wget and download it all.

The moment I saw they posted like thousands of photos, I had to have them. Trying numerous "Flickr downloaders" was disappointing to say the least, so I wrote my own script under an hour. Decided to publish it, so I refined it a bit and here it is!

## How to use it

You need Python 3.x for any platform. Windows, OS X and GNU/Linux should all work. (I tested only on Debian.)

You also need some file downloader that can load up a list of files to download like wget, curl or FDM for Windows.

Download the script or clone the repo and just run it with `python3 pyApolloDL.py`

It creates a file with a list of direct links which you then give to wget: `wget -nc -i photolinks.lst`

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
[*] Extracting direct links from page 1...
[*] Extracting direct links from page 2...
[*] Extracting direct links from page 3...
[*] Extracting direct links from page 4...
[*] Extracting direct links from page 5...
[*] Extracting direct links from page 6...

...

[*] Writing links to 'photolinks.lst'...
[*] Done! Use `wget -nc -c -i photolinks.lst` to download.
```

Now just use wget or whatever to download the pics.

```
$ wget -nc -c -i photolinks.lst
```

> Note: '-nc' stands for "no clobber" and it will tell wget not to overwrite any existing files. '-c' stands for "continue", which continues downloading unfinished files. These two switches together make it easy to continue downloading in case your internet connection breaks.

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

If you give enough of a shit, feel free to submit patches, I'm happy to accept them as I probably won't be improving this script much unless there's some serious bug I haven't noticed, or until I need it again for some other Flickr downloads.

I would also like to thank [FredrikAugust](https://github.com/FredrikAugust) for contributing by optimizing my `writeLinksToFile()` function ([commit here](https://github.com/JackFrancisD/pyApolloPhotosDownloader/commit/9d7501bbdeb0a7e6888e5154aa006c4efac01d61)) because I just didn't do any optimizations.

Cheers,

JackFrancisD
