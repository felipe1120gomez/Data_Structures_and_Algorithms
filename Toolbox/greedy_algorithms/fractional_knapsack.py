# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    '''Given bag capacity, item weight, and item value find the most valuable combination
    of items assuming that any fraction of a loot item can be put into the bag.'''

    total = 0.
    value_item = [float(v) / float(w) for v, w in zip(values, weights)]#Get the value per unit of weight
    num_items = len(values)

    for _ in range(num_items):
        index = value_item.index(max(value_item, default=0))#Obtain the item with the best value / weight ratio
        if capacity == 0:
            return total
            break
        add_capacity = min(capacity, weights[index])#Do not add more weight than allowed
        total += add_capacity * value_item[index]#Item or fraction of item added
        weights[index] -= add_capacity#Fraction extracted from item
        capacity -= add_capacity#Reduced bag capacity after adding
        value_item[index] = 0#The item is converted to zero so as not to choose again

    return total

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, bag = data[0:2]
    value = data[2:(2 * n + 2):2]
    weight = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(bag, weight, value)
    print("{:.10f}".format(opt_value))
