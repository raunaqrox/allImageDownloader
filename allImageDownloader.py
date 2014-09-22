import requests
from bs4 import BeautifulSoup
from StringIO import StringIO
from PIL import Image
import os
import urlparse


def isAbsolute(url):
	return bool(urlparse.urlparse(url).netloc)

print "1.Enter url 2.Enter path(default where script is in folder allDownloadedImages/)"
path = "allDownloadedImages/"
option = raw_input()
if option == '1':
	print "Enter url"
	url = raw_input()
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	images = soup.find_all('img')
	print images	
	for i in images:
		imageName = i.get('alt')
		imageUrl = i.get('src')
		if not isAbsolute(imageUrl):
			imageUrl = urlparse.urljoin(url,imageUrl)
		extension = imageUrl.split('.')
		extension = extension[len(extension)-1]
		r = requests.get(imageUrl)
		image = Image.open(StringIO(r.content))
		if not os.path.exists(path):
			os.makedirs(path)
		image.save(path+imageName+'.'+str(extension))
elif option == '2':
	print "Enter new path"
	path = raw_input()
else:
	quit()
