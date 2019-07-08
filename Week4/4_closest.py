#Uses python3
import sys
import math

def minimum_distance(pts):
	if len(pts)==2:
		return distance(pts[0],pts[1])
	elif len(pts) == 3:
		return min(distance(pts[0],pts[1]),distance(pts[2],pts[1]),distance(pts[0],pts[2]))
	if len(pts)<2:
		return 0	
	d1 = minimum_distance(pts[:len(pts)//2])
	d2 = minimum_distance(pts[len(pts)//2:])
	d = min(d1,d2)
	mid = (pts[len(pts)//2][0] + pts[len(pts)//2+1][0])/2
	s1 = [i for i in pts if abs(mid-i[0])<d]
	if len(s1)==0:
		return d
	s1.sort(key = lambda x: x[1])
	for i in range(len(s1)-1):
		j = 0
		while i+j+1<len(s1)  :
			if(j>5): break
			j+=1
			d = min(d,distance(s1[i],s1[i+j]) )
	return d	




def distance(pts1,pts2):
	return math.sqrt((pts1[0] - pts2[0])**2 + (pts1[1] - pts2[1])**2 )


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    pts = list(zip(x,y))
    pts.sort(key = lambda x:x[0])
    print("{0:.9f}".format(minimum_distance(pts)))
