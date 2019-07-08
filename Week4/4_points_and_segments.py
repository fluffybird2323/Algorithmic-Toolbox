# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts.sort()
    ends.sort()
    n = len(ends)
    for i in range(len(points)):
        l = b_search(starts,points[i]) 
        while l+1< len(starts) and starts[l+1]== points[i]   :
            l+=1
        if  l<len(starts) and starts[l] <= points[i]:
            l+=1    
        r1 =  b_search(ends,points[i])
        while ends[r1-1]== points[i] and r1>0:
            r1-=1
        r = n - r1  
        cnt[i] = l+r-n




    
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt    

def b_search(a,x):
    low = 0
    high = len(a) -1
    while low<= high:
        mid = (low+high)//2
        if(a[mid] == x):
            return mid+1
        elif (a[mid]<x):
            low = mid+1
        else:
            high = mid-1        
    if x>a[mid]:
        return mid+1
    return mid  



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
       print(x, end=' ')
