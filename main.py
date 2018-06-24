from searcher import Searcher
import numpy as np
import argparse
import pickle
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path to the directory that contains the images indexed")
ap.add_argument("-i", "--index", required = True, help = "Path to stored index")
args = vars(ap.parse_args())

index = pickle.load(open(args["index"], "rb"))
searcher = Searcher(index)

#print (index)

for (query, queryFeatures) in index.items():
	
	print (query)
	results = searcher.search(queryFeatures)
	path = args["dataset"] + "/%s" % (query)
	#path = query
	print (path)
	queryImage = cv2.imread(path)
	#print (queryImage.size())
	#queryImage = cv2.resize(queryImage, (300, 300))
	cv2.imshow("Query", queryImage)
	#print ("query: %s" % (query))
	
	#montageA = np.zeros((166 * 5, 400, 3), dtype = uint8)
	#montageB = np.zeros((166 * 5, 400, 3), dtype = uint8)
	
	montageA = np.zeros((300 * 5, 300, 3), dtype = np.uint8)#, dtype = int32)
	montageB = np.zeros((300 * 5, 300, 3), dtype = np.uint8)#, dtype = int32)
	
	for j in range(0, 10):
		
		(score, imageName) = results[j]
		path = args["dataset"] + "/%s"  % (imageName)
		print(path)
		result = cv2.imread(path)
		#result = cv2.resize(result, (300, 300))
		print ("\t%d. %s : %.3f" % (j + 1, imageName, score))
		
		if j < 5:
			montageA[j * 300:(j + 1) * 300, :] = result
			
		else:
			montageB[(j - 5) * 300:((j - 5) + 1) * 300, :] = result

	print ("out")

	cv2.imshow("Results 1-5", montageA)
	cv2.waitKey(0)
	cv2.imshow("Results 6-10", montageB)
	cv2.waitKey(0)
		