import argparse

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
    #knapsack_table = [[0 for x in range(n)] for x in range(maximum_weight+1)]
    for r in range(n):
        print(str(r))

    #knapsack_table = [[None for x in range(maximum_weight+1)] for y in range(n)]
    knapsack_row = [None] * (maximum_weight+1)
    knapsack_table = [knapsack_row] * n
    #knapsack_table = [[None]*maximum_weight+1]*maximum_weight

    print(str(len(knapsack_table)))
    for i in range(n):
        for j in range(maximum_weight + 1):
            knapsack_table[i][0] = 0
            print("i:", i, "j:", j)
            knapsack_table[0][j] = 0 if j < items[0].weight else items[0].value
    for i in range(n):
        for j in range(maximum_weight + 1):
            if j < items[i].weight:
                knapsack_table[i][j] = knapsack_table[i-1][j]
            else:
                #print(str(items[i].value))
                #print(knapsack_table[j-1][j-items[i].weight])
                knapsack_table[i][j] = max(knapsack_table[i-1][j], knapsack_table[i-1][j-items[i].weight] + items[i].value)

    print(str(knapsack_table[n-1][maximum_weight]))
    return knapsack_table[n-1][maximum_weight]


def knapsack_greedy_decreasing_value():
    pass

def knapsack_greedy_increasing_weight():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("itemCount", type=int,
            help="Amount of available items to put into the bag")
    parser.add_argument("maxWeight", type=int,
            help="Maximum weight that can be held in the bag")
    args = parser.parse_args()

    

    items = [Item(2, 3), Item(3, 5), Item(8, 16)]
    maxWeight = args.maxWeight
    knapsack_dynamic(items, maxWeight)



