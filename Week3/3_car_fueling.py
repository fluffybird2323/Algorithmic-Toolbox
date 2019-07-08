# your code goes here# python3
import sys


def compute_min_refills(distance, tank, stops):
	refils = 0
	currentpos = 0
	nextpos=0
	stops.append(distance)
	stops.insert(0,0)
	while stops[currentpos]+tank<distance:
		currentpos=nextpos
		#print(stops[currentpos])
		while  nextpos<len(stops) -1 and stops[nextpos+1]  <=stops[currentpos]+tank :
			nextpos = nextpos+1
	    
		if stops[currentpos]+tank<distance:
			refils+=1
		if nextpos==currentpos:
			return -1
	
	
	return refils	


    	



if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
