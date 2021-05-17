# python3
import sys

def compute_min_refills(distance, tank, stops):
    '''Given total distance, tank capacity, and location of the gas stations,
    find out what is the minimum number of refills needed to cover the total distance.'''

    travel = len(stops)

    if tank >= distance:#Tank greater than distance = 0 stops
        return 0

    if tank >= distance and travel == 0:#Tank greater than distance and 0 stops = 0 stops
        return 0

    elif tank < distance and travel == 0:
        return -1#Tank less than distance and 0 stops = impossible

    #Tank smaller than first station or smaller than distance between last station and destination = impossible
    if tank < stops[0] or tank < (distance - stops[-1]):
        return -1

    for i in range(travel):

        if i == travel - 1:#Avoid Index error
            break

        next_i = stops[i + 1]#Next station

        between = next_i - stops[i]#Distance between two stations

        if tank < between:#If tank is less than distance between any two stations = impossible
            return -1
            break

    breaks = 0
    refill = tank#Maximum tank capacity
    for i in range(travel):

        if i == 0:
            prev_i = 0#Starting point

        else:
            prev_i = stops[i - 1]#Previous station

        cur_i = stops[i]#Current station

        if i == travel - 1:#Avoid index error
            next_i = distance#Destination

        else:
            next_i = stops[i + 1]#Next station

        #If tank minus distance already traveled is greater than or equal to distance to travel
        if tank - (cur_i - prev_i) >= (next_i - cur_i):
            tank -= (cur_i - prev_i)#Tank minus distance already traveled
            continue#Next station

        #Otherwise refill to be able to reach that distance
        tank = refill#Fill the tank, !do not exceed its capacity
        breaks += 1

    return breaks

if __name__ == '__main__':
    d, m, _, *stations = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stations))
