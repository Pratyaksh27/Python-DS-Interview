list = [1,2,3,5,6,7,8,9,20,75,100]

def bin_search(list, start, end, value):
    if not list or end < start:
        print("No List")
        return None
    mid = (start+end)//2
    if list[mid] == value:
        return mid
    if list[mid] < value:
        return bin_search(list, mid+1, end, value)
    else:
        return bin_search(list, start, mid-1, value)

print("Lenght ", len(list))
print(" Index of 5 is ", bin_search(list, 0, len(list)-1, 5))
print(" Index of 1 is ", bin_search(list, 0, len(list)-1, 1))
print(" Index of 100 is ", bin_search(list, 0, len(list)-1, 100))
print(" Index of 2 is ", bin_search(list, 0, len(list)-1, 2))
print(" Index of 20 is ", bin_search(list, 0, len(list)-1, 20))
print(" Index of 4 is ", bin_search(list, 0, len(list)-1, 4))
print(" Index of -1 is ", bin_search(list, 0, len(list)-1, -1))
print(" Index of 101 is ", bin_search(list, 0, len(list)-1, 101))
