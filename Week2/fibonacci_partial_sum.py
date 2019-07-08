# your code goes here# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    a=get_fibonacci_huge_naive(from_+1, 10) 
    b=get_fibonacci_huge_naive(to+2, 10) 
    c = b-a
    if(c<0):
    	return c + 10
    else:
    	return c	

def pisanoperiod(a):
    period = 0
    index=0
    c = 0 
    b = 1
    for i in range(1,len(a)):
        if((a[i]==0) & (a[i+1]==1)):
            break
    index = i
    return index

def get_fibonacci(m): 
    x = m*m+1
    a = list()
    a0=0
    a1=1
    a.append(a0)
    a.append(a1)
    for i in range(x):
        a0,a1 = a1,(a0+a1)%m
        a.append(a1)
    return(a)    
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    a = pisanoperiod(get_fibonacci(m))
    previous = 0
    current  = 1
    g = n%a
    if g <= 1:
        return g

    for i in range(g-1):
        previous, current = current, previous + current
        if i % 10 == 0:
            previous, current =  previous , current
    return (current) %m  


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))



  