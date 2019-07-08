# your code goes here# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    index=0
    segments.sort(key=lambda x:x[1])
    covered= [0]*len(segments)
    for i in range(len(segments)):
    	if covered[i]==0:
    		points.append(segments[i][1])
    		index=0
    		for j in segments:
    			covered[index] = point_in(j[0],j[1],segments[i][1])
    			index+=1
    	#print(covered)
    return points			



def point_in(x1,x2,pnt):
	if pnt>=x1 and pnt <=x2:
		return 1
	return 0 	


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
