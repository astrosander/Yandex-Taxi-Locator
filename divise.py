def Devise(PointA, PointB, DefDiff):
	coord = []
	xNum = int((PointB[0] - PointA[0])/DefDiff)
	yNum = int((PointB[1] - PointA[1])/DefDiff)

	for x in range(xNum):
	    xPoint = PointA[0] + (PointB[0] - PointA[0]) * x / (xNum - 1)
	    for y in range(yNum):        
	        yPoint = PointA[1] + (PointB[1] - PointA[1]) * y / (yNum - 1)
	        coord.append([xPoint, yPoint])

	return coord