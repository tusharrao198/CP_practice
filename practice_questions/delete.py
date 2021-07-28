from itertools import *
lst = [1,2,3,4,5,6]
prefix_sum = accumulate(lst)
print([i for i in prefix_sum])