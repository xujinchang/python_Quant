from numpy import *

def euclDis(v1, v2):
	return sum(power(v1 - v2, 2))

def initCentroids(dataset, k):
	numSamples, dim = dataset.shape
	print numSamples, dim
	centroids = zeros((k + 1, dim))
	for i in range(1, k + 1):
		index = int(random.uniform(0, numSamples))
		centroids[i, :] = dataset[index, :]
	return centroids

def kmeans(dataset, k):
	numSamples = dataset.shape[0]
	clusterAssment = mat(zeros((numSamples, 2)))
	clusterChanged = True
	for i in xrange(1, numSamples):
		clusterAssment[i, 0] = -1
	#step 1
	centroids = initCentroids(dataset, k)

	while clusterChanged:
		clusterChanged = False

		for i in xrange(numSamples):
			minDist = 100000.0
			minIndex = 0

			#step 2 for each centroid, find the closest centroid 
			for j in range(1, k + 1):
				distance = euclDis(centroids[j, :], dataset[i, :])
				if distance < minDist:
					minDist = distance
					minIndex = j
			#step 3 update cluster
			if clusterAssment[i, 0] != minIndex:
				clusterChanged = True
				clusterAssment[i, :] = minIndex, minDist
			else:
				clusterAssment[i, 1] = minDist
				
		#step4 update centroids
		for j in range(1, k + 1):
			pointsCluster = dataset[nonzero(clusterAssment[:, 0].A == j)[0]] # matrix.A Return self as an ndarray object.
			centroids[j, :] = mean(pointsCluster, axis = 0)
	return centroids, clusterAssment


if __name__ == '__main__':
	print "step 1: load data..."  
	dataSet = []  
	fp = open('testSet.txt')  
	for line in fp.readlines():
		lineArr = line.strip().split(' ')
		dataSet.append([float(lineArr[0]), float(lineArr[1])])
	print "step 2: clustering..."
	dataSet = mat(dataSet)  
	print "dataSet:"  
	print dataSet  
	k = 4  
	centroids, clusterAssment = kmeans(dataSet, k)

	print "center:"  
	print centroids  
	print "clusterAssment:"  
	print clusterAssment  
	


