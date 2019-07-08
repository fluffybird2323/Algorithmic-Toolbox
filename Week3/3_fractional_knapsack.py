# your code goes here# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    maxim = 0
    pindex = list()
    index = 0
    while capacity>0:
        maxim = 0
        for i in range(len(weights)):
            if values[i]/weights[i]>=maxim and not(i in pindex):
                maxim = values[i]/weights[i]
                index = i

        ic = min(weights[index],capacity)
        capacity -= ic
        
        value += ic*maxim
        pindex.append(index)


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
