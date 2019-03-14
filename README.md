# Installing and Running the Project

## Python Requirements
Please refer to the [Linux/Unix/BSD](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) or the [Windows](https://docs.python.org/3/using/windows.html) python installation manual to install python.

**IMPORTANT** This version of the code only work on Python 3.7+ due to requirements for [time.perf_counter_ns()](https://docs.python.org/3/library/time.html#time.perf_counter_ns). If you're running Python 3.3+ and cannot upgrade, please replace all instances of `time.perf_counter_ns()` with `time.perf_counter()`. This action will also change all the timing to be recorded in seconds rather than nanoseconds.

## Arguments
`python3 knapsack.py -h` for help on arguments.
Usage: `python3 knapsack.py [-h] itemCount maxWeight`
- itemCount :: Amount of available items to put into the bag
- maxWeight :: Maximum weight that can be held in the bag

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
g1err.add(soln/optimal)

start = clock()
soln = greedy1(items, W)
end = clock()
g2times.add(end-start)
g2err.add(soln/optimal)
```

This is only one iteration; you should iterate multiple times (you choose the number of iterations, but it should run multiple times).  You can then average the runtime lists and the error lists to get your average runtimes and qualities.

### Sample IO
```bash
$ python3 knapsack.py 50 200
Parameters:
-- ITERS: 100
-- NUM ITEMS: 50
-- BAG MAX WEIGHT: 200
-- MAX ITEM WEIGHT: 200
-- MAX VALUE: 100

Algorithms: DP, Increasing weight, Decreasing wt/val

Results:
Time (DP): 0.0019124223696417176
Time (Greedy 1): 8.813849126454442e-06
Time (Greedy 2): 9.25262167584151e-06
Quality (Greedy 1): 0.8418419025470252
Quality Time (Greedy 2): 0.987260762885207
```

You may also output a table if you want; when you write your report you will be varying either the number of items or the maximum bag weight.  You can make that decision early on and output the same kind of table you did for project 1.  You should print two tables if you take this option: Time and Quality (for either n vs algorithm or W vs algorithm).

### Deliverables

You must submit code that implements the dynamic programming and greedy heuristic approaches to solving this problem, generates random lists of items, and outputs the average timings for a given n (number of items) and W (maximum weight).  You are not to submit a `.zip` file in your git repository (all source code must be visible directly in the repository).  Additionally if you are working with a partner both group members must show contribution through commits to the repository.
