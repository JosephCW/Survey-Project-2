import argparse

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    
    def __repr__(self):
        return 'Weight: {}, Value: {}'.format(self.weight, self.value)

def knapsack_dynamic():
    pass

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

