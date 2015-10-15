#!/bin/env python3
# pyApolloPhotosDownloader v0.1 ALPHA - Flickr downloader
# coded by JackFrancisD <jackfd@openmailbox.org>
################################################################################
import urllib.request


## Global constants you can change #############################################
MAIN_URL = "https://www.flickr.com/photos/projectapolloarchive"
LINKS_LIST_FILENAME = "photolinks.lst"


## Constants ###################################################################
directLinkSearchPattern = "\"o\":{\"displayUrl\""


## Functions and globals #######################################################
finalLinksList = []

def dbg(string):
	print("[*] " + string)
	return


def getPatternLocations(responseString):
	index = 0
	indexList = []
	global directLinkSearchPattern

	while 1:
		index = responseString.find(directLinkSearchPattern, index)
		if index == -1:
			break
		indexList.append(index)
		index += 1
	return indexList


def getDirectLinksFromPage(photostreamHTML):
	indexList = getPatternLocations(photostreamHTML)
	linksList = []
	i=0

	while i < len(indexList):
		part = photostreamHTML[indexList[i]:indexList[i]+90]
		part = part[20:89]
		part = part.replace("\\/\\\\/","https://")
		part = part.replace("\\\\/","/")
		part = part.split("\"")[0]
	#	print(part) # TODO comment out, debug line
		linksList.append(part)
		i += 1
	
	return linksList


def getPageCount(photostreamUrl):
	dbg("Extracting page count...")
	data = str(urllib.request.urlopen(photostreamUrl).read())

	moreDotsIndex = data.find("<span class=\"moredots\"")
	pageCount = data[moreDotsIndex:moreDotsIndex+300]
	pageCount = pageCount[pageCount.find("pagination"):len(pageCount)]
	pageCount = pageCount[pageCount.find("pagination",1):len(pageCount)]
	pageCount = pageCount[10:len(pageCount)]
	pageCount = pageCount.split("C")[0]

	return int(pageCount)


def getAllLinks():
	global finalLinksList
	global MAIN_URL
	linksList = []

	i=1	
	
	pageCount = getPageCount(MAIN_URL)
	dbg(str(pageCount) + " pages found.")

	while i <= pageCount:
		pageUrl = MAIN_URL + "/page" + str(i)
		response = urllib.request.urlopen(pageUrl)
		data = response.read()

		dbg("Extracting direct links from page " + str(i) + "...")
		linksList.append(getDirectLinksFromPage(str(data)))
		#print(linksList) # TODO dbg
		
		finalLinksList = linksList
		i += 1 

	return


def writeLinksToFile():
	buf = ""
	i=0

	dbg("Writing links to '" + LINKS_LIST_FILENAME + "'...")

	f=open(LINKS_LIST_FILENAME,"w")
	
	while i < len(finalLinksList):
		line = finalLinksList[i] + "\n"
		buf += line
		i += 1

	f.write(buf)
	f.close()
	dbg("Done! Use `wget -i " + LINKS_LIST_FILENAME + "` to download.")
	return


## Main ########################################################################
def main():
	print("pyApolloPhotosDownloader v0.1 ALPHA - Flickr downloader")
	print("Coded by JackFrancisD <jackfd@openmailbox.org>")
	print("==========================================================")
	print("[!] This software is an early version. No errors are handled, but it does work.")
	dbg("Starting Flickr direct link extraction from " + MAIN_URL)
	getAllLinks()
	writeLinksToFile()
	exit()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nCtrl-C caught. Quitting..")
		writeLinksToFile()
		exit()
 
