#code from https://stackoverflow.com/questions/5661089/python-compare-two-lists-in-a-comprehension
L1 = ['a', 'b', 'c', 'd']
L2 = ['b', 'c', 'd', 'e']
S1 = set(L1)
S2 = set(L2)
difference = list(S1.symmetric_difference(S2))
print(difference)
