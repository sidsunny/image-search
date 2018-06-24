from RGBHistogram import RGBHistogram
import argparse
#import _pickle as cPickle
import pickle
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True, help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# index is a dictionary, 'key' is a filename and 'value' our computed features
index = {}


# define number of bins
num_bins = [8, 8, 8]
# initialize our image descriptor -- a 3D RGB histogram with
# 8 bins per channel
desc = RGBHistogram(num_bins)

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
 
	# extract our unique image ID (i.e. the filename)
	k = imagePath[imagePath.rfind("\\") + 1:]

	print(k)
	# load the image, describe it using our RGB histogram
	# descriptor, and update the index
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (300, 300))
	cv2.imwrite(imagePath,image)
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

# we are now done indexing our image -- now we can write our
# index to disk
f = open(args["index"], "wb")
pickle.dump(index, f)
#f.write(cPickle.dumps(index))
f.close()