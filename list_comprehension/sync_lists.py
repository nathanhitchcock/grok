# Given two lists, perform syncing of all the elements of list with other list when removal of duplicate elements in first list.

'''
Input : test_list1 = [1, 1, 2, 2, 3, 3], test_list2 = [8, 3, 7, 5, 4, 1] 
Output : [1, 2, 3], [8, 7, 4]
Explanation : After removal of duplicates (1, 2, 3), corresponding elements are removed from 2nd list, and hence (8, 7, 4) are mapped.
Input : test_list1 = [1, 2, 2, 2, 2], test_list2 = [8, 3, 7, 5, 4, 1]
Output : [1, 2], [8, 3]
Explanation : Elements removed are (2, 2, 2), [1, 2] are mapped to [8, 3] as expected.
'''
