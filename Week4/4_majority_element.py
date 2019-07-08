# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left+right)//2
    x = get_majority_element(a,left,mid)
    y = get_majority_element(a,mid,right)

    xcount = get_count(a, mid, right,x) + get_count(a, left,mid,x)
    ycount = get_count(a, left, mid,y)+ get_count(a, mid, right,y)
    if xcount>ycount and xcount > (right-left)//2:
        return x 
    elif ycount>xcount and ycount > (right-left)//2:
        return y
    if x==y :
        return x
    
    return -1
    
    

def get_count(a, left, right,x):
    count = 0
    for i in range(left,right):
        if(a[i]==x):
            count+=1
    return count    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)