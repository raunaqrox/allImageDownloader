#! /usr/bin/env python
import requests
from bs4 import BeautifulSoup
from StringIO import StringIO
from PIL import Image
import os
import urlparse

#global variable path

path = "allDownloadedImages/"


def isAbsolute(url):
	return bool(urlparse.urlparse(url).netloc)

def downloader():
	print "Enter url"
	url = raw_input()
	if url=='':
		quit()
	else:
		html = requests.get(url)
		soup = BeautifulSoup(html.text)
		images = soup.find_all('img')
		print images	
		for i in images:
			imageName = i.get('alt')
			imageUrl = i.get('src')
			if not isAbsolute(imageUrl):
				imageUrl = urlparse.urljoin(url,imageUrl)
			r = requests.get(imageUrl)
			image = Image.open(StringIO(r.content))
			if not os.path.exists(path):
				os.makedirs(path)	
			try:
				imageUrl = imageUrl.split('/')
				imageUrl = imageUrl[len(imageUrl)-1]
				image.save(path+str(imageName)+'_'+str(imageUrl))
			except:
				print "Error on "+ str(imageName)+'_'+str(imageUrl)
				continue

def pathChanger():
	print "Enter new path"
	global path 
	path = raw_input()
	if path[len(path)-1] == '/':
		return
	else:
		path = path+ '/'	

def main():
	print "1.Enter url 2.Enter path(default where script is in folder allDownloadedImages/)"

	option = raw_input()
	if option == '1':
		downloader()
	elif option == '2':
		pathChanger()
		downloader()
	else:
		quit()
if __name__ == '__main__':
	main()
