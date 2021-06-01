# Cross List Sync on duplicate elements removal
# Using loop + dict()

# initializing the lists
test_list1 = [2, 2, 3, 4, "test", 4, 5, 5, 6, 6, "test"]
test_list2 = [8, 3, 7, 5, 4, 1, 0, 9, 4, 2, 2, 2, 2, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2) + "\n")

# coss list sync; remove dupliacte elements
temp_dict = dict()
temp_list = []

# iterate through the length of the list
for i in range(len(test_list1)):
    # if the item is not in the temp_list, add it
    if test_list1[i] not in temp_list:
        temp_list.append(test_list1[i])

        # memoize for optimization
        temp_dict[test_list1[i]] = test_list2[i]

result2 = list(temp_dict.values())
result1 = temp_list

# printing result
print("List 1 : " + str(result1))
print("List 2 : " + str(result2))
print("Combined Sync List : " + str(result1 + result2))
