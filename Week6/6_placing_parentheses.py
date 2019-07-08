# your code goes here# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
	d = dataset[::2]
	op = dataset[1::2]
	d=[float(i) for i in d]
	m = [[0]*(len(d)+1) for _ in range(len(d)+1)]
	M = [[0]*(len(d)+1) for _ in range(len(d)+1)]
	for i in range(1,len(d)+1):
		m[i][i] = M[i][i] = d[i-1]
	n = len(d)
	for s in range(1,n):
		for i in range(1,n-s+1):
			j = i+s
			mini,maxi = float('inf'),float('-inf')
			for k in range(i,j):
				a = evalt(M[i][k],M[k+1][j],op[k-1])
				b = evalt(M[i][k],m[k+1][j],op[k-1])
				c = evalt(m[i][k],M[k+1][j],op[k-1])
				d = evalt(m[i][k],m[k+1][j],op[k-1])
				mini = min(mini,a,b,c,d)
				maxi = max(maxi,a,b,c,d)
			m[i][j] = mini
			M[i][j]	= maxi
	return M[1][n]


if __name__ == "__main__":
    print(get_maximum_value(input()))
