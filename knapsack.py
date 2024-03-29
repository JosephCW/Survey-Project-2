#!/bin/python3

# 0-1 Knapsack Python Implementation and Analyzer
# Authors: Daiwei Chen  (@ForeverAnApple)
#          Joseph Watts (@JosephCW)
# Version: 2019-03-13

import argparse
import time
import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return 'Weight: {}, Value: {}'.format(self.weight, self.value)

def knapsack_dynamic(items, maximum_weight):
    # Number of items in list
    n = len(items)
    # 2d array with n rows and n+1 columns
    # knapsack_table at [i][j] represents optimal value with # of items being i, and j representing maximum weight
    # Note, this is a VERY LARGE array.
    knapsack_table = [[0 for i in range(maximum_weight + 1)]
                      for y in range(n)]

    for i in range(n):
        for j in range(maximum_weight + 1):
            knapsack_table[i][0] = 0
            knapsack_table[0][j] = 0 if j < items[0].weight else items[0].value
    for i in range(n):
        for j in range(maximum_weight + 1):
            if j < items[i].weight:
                knapsack_table[i][j] = knapsack_table[i-1][j]
            else:
                knapsack_table[i][j] = max(knapsack_table[i-1][j], knapsack_table[i-1][j-items[i].weight] + items[i].value)

    return knapsack_table[n-1][maximum_weight]

def knapsack_greedy_grab(items, max_wt):
    sigmaValue = 0

    for item in items:
        if item.weight <= max_wt:
            max_wt -= item.weight
            sigmaValue += item.value
        if max_wt == 0:
            return sigmaValue
    return sigmaValue

# Hi I'm Greedy Greedman, and I'm a collector of interesting trinkets of
# high to moderately high value.
def knapsack_greedy_weight(items, max_wt, decreasing=False):
    items_sorted = sorted(items,
                          key=lambda item: item.weight,
                          reverse=decreasing)
    return knapsack_greedy_grab(items_sorted, max_wt)

# Sup y'all it's Greedy Greedman coming at cha, once again we have another
# night stream. Unfortunately our last stream had to be cut short due
# to a run in with the cops, but after 3 weeks on probation I'm out here
# with another one.
def knapsack_greedy_value(items, max_wt):
    items_sorted = sorted(items,
                          key=lambda item: item.value,
                          reverse=True)
    return knapsack_greedy_grab(items_sorted, max_wt)

# Hey guys, Greedy Greedman here once again, coming at ya with another
# house tour, it's not my house but the owners were nice enough to leave
# the front doors unlocked.
def knapsack_greedy_ratio(items, max_wt):
    items_sorted = sorted(items,
                          key=lambda item: item.value/item.weight,
                          reverse=True)
    return knapsack_greedy_grab(items_sorted, max_wt)

# wt and value are tuples of (min_value, max_value)
def generate_items(count, wt, vl):
    itemlist = []
    for i in range(count):
        itemlist.append(Item(random.randrange(wt[0], wt[1]+1),
                             random.randrange(vl[0], vl[1]+1)))

    return itemlist

# Printing parameters
def print_parameters(tCount, iCount, max_wt, wt_range, vl_range):
    print("Timing Parameters:")
    print("--- Trial Count:\t", tCount)
    print("--- Item Count:\t\t", iCount)
    print("--- Max Weight:\t\t", max_wt)
    print(f"--- Weight Range:\t {wt_range[0]} - {wt_range[1]}")
    print(f"--- Value Range:\t {vl_range[0]} - {vl_range[1]}")
    print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("itemCount", type=int,
            help="Amount of available items to put into the bag")
    parser.add_argument("maxWeight", type=int,
            help="Maximum weight that can be held in the bag")
    args = parser.parse_args()

    maxWeight = args.maxWeight
    itemCount = args.itemCount
    trials = 100
    # Parameters of item generation weight and value
    itemgen_wt = (1, 10)
    itemgen_vl = (1, 25)

    print_parameters(trials, itemCount, maxWeight, itemgen_wt, itemgen_vl)

    dptimes, gwtimes, gvtimes, grtimes, gwerr, gverr, grerr = (
        [] for i in range(7))

    times = (gwtimes, gvtimes, grtimes)
    errs  = (gwerr, gverr, grerr)
    greed = (knapsack_greedy_weight,
             knapsack_greedy_value,
             knapsack_greedy_ratio)

    # N E X T 👏 A L G O 👏
    for i in range(trials):
        items = generate_items(itemCount, itemgen_wt, itemgen_vl)

        start = time.perf_counter_ns() # The perfect counter.
        optimal = knapsack_dynamic(items, maxWeight)
        dptimes.append(time.perf_counter_ns()-start)

        for j in range(3):
            start = time.perf_counter_ns()
            greed_out = greed[j](items, maxWeight)
            times[j].append(time.perf_counter_ns() - start)
            errs[j].append(greed_out / optimal)

    # Output results
    print("Algorithms tested: DP, Increasing Weight, Decreasing Value, and Decreasing Ratio (value/weight)\n\nAll times are recorded and shown in nanoseconds.\nSorting times are included within runtime.\n")
    algos = ["Increasing Weight", "Decreasing Value", "Decreasing Ratio (value/weight)"]
    print("Recorded Data:")
    print("Runtime (DP):", sum(dptimes)/len(dptimes))
    for i in range(3):
        print("-----------------------")
        print(f"Showing Data for {algos[i]}")
        print(f"Runtime  (Greedy): {sum(times[i])/len(times[i])})")
        print(f"Accuracy (Greedy): {sum(errs[i])/len(errs[i])*100:.4f}%)")
