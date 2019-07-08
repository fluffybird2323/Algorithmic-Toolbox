# Uses python3
def edit_distance(s, t):
    T = [[100]*(len(s)+1) for _ in range(len(t)+1)]
    for i in range(len(s)+1):
    	T[0][i] = i
    for j in range(len(t)+1):
    	T[j][0] = j
    for i in range(1,len(t)+1):
    	for j in range(1,len(s)+1):
    		diff = 0 if s[j-1]==t[i-1] else 1
    		T[i][j] = min(T[i-1][j]+1,T[i][j-1]+1,T[i-1][j-1]+diff)


    return T[i][j]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
