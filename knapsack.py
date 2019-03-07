
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


item1 = Item(4, 5)
print(item1)
