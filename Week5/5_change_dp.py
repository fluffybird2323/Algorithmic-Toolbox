# your code goes here# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [0]*(m+1)
    coins[0] = 0
    for i in range(1,m+1):
    	if i <3:
    		coins[i] = i
    	

    	elif i <5 :
    		coins[i] = 1
    	

    	else:
    		coins[i] = min(coins[i-1],coins[i-3],coins[i-4])+1

    return coins[m]		



    return 

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
