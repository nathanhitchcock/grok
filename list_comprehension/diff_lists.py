# initalize the lists
# TODO - test with ACL logic, this may tigger on unordered objects,
#   batfish solves for the unordered object issue by using extrapolated dataset
li1 = [10, 15, 20, 25, 30, 35, 40, "test", "test_3"]
li2 = [20, 40, 35, "test", "test_2"]

# algorithm that gets difference of two lists
def diff(li1, li2):
    """
    iterate over the list objects (i,i); combining the two lists as the dataset.
    if i does not appear in either list, add it to the li_dif list.
    """
    li_dif = [
    i for i in li1 + li2
        if i not in li1 or i not in li2
    ]
    # return the obects that are no in either list
    return li_dif

if __name__ == "__main__":

    print("the original lists are : ", "\n", li1, "\n", li2)

    result = diff(li1, li2)

    print("\n", "the resulting list of diff objects is: ", "\n", result)
