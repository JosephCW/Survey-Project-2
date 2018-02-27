# Project 02

## 44-349 Survey of Algorithms

For this project you are to implement multiple solutions (both heuristic and dynamic programming) for the 0-1 Knapsack Problem.
You will be comparing both the runtime and relative quality of the solutions you implement.

### Problem Definition

Input: a list of items (each with an associated integer weight and value), and a maximum weight `W`.

Output: The maximum value of the subset of items whose total weight does not exceed `W`

You have a magical knapsack that can carry any volume of items, but is limited to a maximum weight `W`.  You are considering a list of items, and want to know the maximum value of the items you can fit in the bag.

How you choose to represent your item is up to you.  You can use a list of items, or lists of values and weights, or some other interesting representation that makes it easy to solve the problems.

### Dynamic Programming

The dynamic programming solution builds a table from which one can read the solution.  Given `n` items and a knapsack that can carry `W` units of weight, the table is a two dimensional array (`K`) with `n` rows and `W + 1` columns.
`K[i][j]` has the meaning: the optimal value when considering the items through index `i` and the knapsack has maximum weight `j`.

For the following definitions, assume that items is an array, with each element having a `val` and `wt` attribute

The first row can column can be populated:

```
K[i][0] = 0
K[0][j] = 0 if j < items[0].wt, items[0].val otherwose
```

The remaining elements can be calculated as:

```
if j < items[i].wt
    K[i][j] = K[i-1][j]
else
    K[i][j] = max(K[i-1][j], K[i-1][j-items[i].wt] + items[i].val)
```

The optimal value can then be read from `K[n-1][W]`

### Greedy Heuristic

You must implement two greedy heuristics.  You should choose two of the following choices:

* Sort by decreasing value and take as many items as possible
* Sort by increasing weight and take as many items as possible
* Sort by decreasing value to weight ratio and take as many items as possible

### Timing and Comparing

You need to compare both the quality and the runtime of these different solutions.  To compare quality, we will use the Relative Error.  This can make your measurements tricky, as you will need to use the same set of items for each of your implementations.  One way to do this (assume that you have lists `dptimes`, `g1times`, `g2times`, `g1err`, `g2err`) (assume that clock() is the way to get your timer in whatever programming language you use)

```
items = new list of items (randomized)
start = clock()
optimal = knapsack(items, W)
end = clock()
dptimes.add(end-start)

start = clock()
soln = greedy1(items, W)
end = clock()
g1times.add(end-start)
g1err.add((optimal - soln)/optimal)

start = clock()
soln = greedy1(items, W)
end = clock()
g2times.add(end-start)
g2err.add((optimal - soln)/optimal)
```

This is only one iteration; you should iterate multiple times (you choose the number of iterations, but it should run multiple times).  You can then average the runtime lists and the error lists to get your average runtimes and qualities.

Sample expected output will be provided in class.

### Deliverables

You must submit code that implements the dynamic programming and greedy heuristic approaches to solving this problem, generates random lists of items, and outputs the average timings for a given n (number of items) and W (maximum weight)