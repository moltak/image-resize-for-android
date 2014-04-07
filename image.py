from os import listdir
from os.path import isfile, join
import os
import shutil
from PIL import Image
import string

xxhdpi = './drawable-xxhdpi/'
xhdpi = './drawable-xhdpi/' 
hdpi = './drawable-hdpi/'
mdpi = './drawable-mdpi/'
 
def makeEachDpiFolders(dpi):
  if os.path.exists(dpi) == False:
		os.makedirs(dpi)
 
def resizeFile(image_file, dpi, ratio):
	print 'resizing ' + image_file
	im = Image.open(xxhdpi + image_file)
	width = int(im.size[0] * ratio)
	height = int(im.size[1] * ratio)
	newim = im.resize((width, height), Image.ANTIALIAS)
	outfile = dpi + image_file
	newim.save(outfile, 'PNG')
	printCopySummary(im, width, height, outfile)
 
def printCopySummary(im, width, height, outfile):
	print ("%s w: %d->%d h: %d->%d" % (outfile, im.size[0], width, im.size[1], height))

makeEachDpiFolders(xhdpi)
makeEachDpiFolders(hdpi)
makeEachDpiFolders(mdpi)

onlyfiles = [f for f in listdir(xxhdpi) if isfile(join(xxhdpi,f))]
copycount = 0
 
for f in onlyfiles:
	file_extension = f.split('.')[1]
	if (string.upper(file_extension) == 'PNG') | (file_extension == '9'):
		resizeFile(f, xhdpi, 2/3)
		resizeFile(f, hdpi, 1/2)
		resizeFile(f, mdpi, 1/3)
		copycount += 1
 
print ('\ndone: %d files' % copycount)