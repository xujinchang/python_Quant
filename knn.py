import numpy as np
from numpy import *
import operator


def createDataSet():
    group = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels = ['A','A','B','B']
    return group,labels




def classify(input, dataset, label, k):
 	datasize = dataset.shape[0]
 	## eclucian
 	diff =  tile(input, (datasize,1)) - dataset
 	sqdiff = diff ** 2
 	squareDist = sum(sqdiff, axis=1) #hang xiangliang
 	dist = squareDist ** 0.5 

 	sortedDistIndex = argsort(dist)

 	classCount = {}
 	for i in range(k):
 		voteLabel = label[sortedDistIndex[i]]
 		classCount[voteLabel] = classCount.get(voteLabel,0) + 1
 	maxCount = 0
 	for key, value in classCount.items():
 		if value > maxCount:
 			maxCount = value
 			classes = key
 	return classes

if __name__ == '__main__':
	dataset, labels = createDataSet()
	input = array([1.1, 0.3])
	K = 3
	output = classify(input, dataset, labels, K)
	print(output)