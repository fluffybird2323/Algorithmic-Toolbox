# your code goes here# Uses python3
import sys

def optimal_summands(n):
    summands = []
    csum=0
    pr=0
    for i in range(n):
    	pr+=1
    	if(csum>=n):
    		break
    	r = opsummands(n,pr,csum)
    	summands.append(r)
    	csum+=r	
    
    return summands
def opsummands(n,lb,csum):
	if (csum+lb+lb+1)>n:
		return n-csum
	return lb	


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
