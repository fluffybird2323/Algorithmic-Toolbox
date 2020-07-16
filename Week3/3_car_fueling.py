# your code goes here# python3
import sys

def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    no_stops = 0
    left_dist = distance
    covered_dist = 0
    for i in range(len(stops) - 1):
        if (left_dist == 0):
            break
        elif ((stops[i + 1] - stops[i]) > tank):
            no_stops = -1
            break
        elif ((covered_dist + tank) >= stops[i] and (covered_dist + tank) < stops[i + 1]):
            covered_dist = stops[i]
            left_dist = distance - stops[i]
            no_stops +=  1
    return no_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
