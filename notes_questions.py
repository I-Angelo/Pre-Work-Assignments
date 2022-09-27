print('\n\nQuestion # 1 :....\n\n')

def hello_name(user_name):
    """This finction greets the user"""
    print('hello_' + user_name + '!')

hello_name('USERNAME')
print('\n')
hello_name('Ivan!!')


print('\n\nQuestion # 2 : .....\n\n')

def first_odds():
    """This function print odd numbers from 1-100"""
    for i in range(1, 100):
        if i % 2 == 1:
            print(i)
            

first_odds()


print('\n\nQuestion # 3 : .....\n\n')


def max_num_in_list(a_list):
    return max(a_list)
    
print('The MAX number on the list provided is : ', end='')
print(max_num_in_list([1,2,3,4,5,1267,6,7,8,9,20,11,12,13,14,15,16,17,18,67]))


print('\n\nQuestion # 4 : .....\n\n')


def is_leap_year(a_year):
    if (a_year % 400) == 0:
        return True
    elif (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    else:
        return False




print(bool(is_leap_year(2200)))


print('\n\nQuestion # 5 : .....\n\n')

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



print('\n\nEND OF ALL QUESTIONS.....\n\n\n')
