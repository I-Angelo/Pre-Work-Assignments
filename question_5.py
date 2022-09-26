from hashlib import new


def is_consecutive(a_list):
    new_list = sorted(a_list)
    if new_list == list(range(min(new_list), max(new_list) + 1)):
        return True
    else:
        print(new_list)
        print(list(range(min(new_list), max(new_list) + 1))) ##This line of code takes the smallest number in the list and the largest and makes a whole new list
                                                            ## From the smallest number to the lartgest in order as it is printed below
                                                            # then compares it to the 'new_list that is the sorted() original list which does not
                                                            # contain as many numbers and are far from consecutive. I printed them both for demostration 
                                                            # purposes. The '+1' in range() is because range() stop parameter is not inclusive.
        return False
        

    

print(bool(is_consecutive([2,25,3,7,5])))