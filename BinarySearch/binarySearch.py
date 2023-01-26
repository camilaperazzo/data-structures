# Basic Binary Search Alghoritm 
# 
def binarySearch(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low +high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess> item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_List = [30, 5, 2, 0, 1]

print (binarySearch(my_List, 1))
print (binarySearch(my_List, 15))
