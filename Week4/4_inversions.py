# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions = get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a,b,left,right)
    return number_of_inversions

def merge(a,b,left,right):
	mid = (left+right)//2

	#1st while loop runs as long as any subarray has
	#elements left and inversion occurs if a[i] > a[j]
	#no of inversions is mid - j
	inv_count = 0
	i=left
	j=mid
	k=left
	while i<mid and j<right:
		if a[i]<=a[j]:
			#no inversion
			b[k] = a[i]
			i+=1
			k+=1
		else : #inversion occurs
			inv_count+=mid-i
			b[k] = a[j]
			k+=1
			j+=1

	
	while i<mid :
		b[k] = a[i]
		i+=1
		k+=1
	while j<right :
		b[k] = a[j]
		k+=1
		j+=1

	for ind in range(left,right):
		a[ind] = b[ind]

	
	return inv_count	


				






if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
