# Input: Sorted Array But with 0s interspersed
# Output: Find an element's position

list = [1,2,0,0,0,0,0,4,8,9,20,0,21,0,0,99,0,0]

def bin_search_sparsed_array(list, start, end, value):
    if not list or end < start:
        return None
    mid = (start+end)//2
    print(" Mid is ", mid, " Value is ", list[mid])
    if list[mid]==value:
        return mid
    if list[mid]!=0 and list[mid]<value:
        print("Searching again with indixes ", mid+1, " and ", end, " list mid is ",list[mid], " Value is ", value)
        return bin_search_sparsed_array(list, mid+1, end, value)
    elif list[mid]!=0 and list[mid]>value:
        print("Searching again with indices ", start, " and ", mid-1, " list mid is ", list[mid], " value is ", value)
        return bin_search_sparsed_array(list, start, mid-1, value)
    elif list[mid]==0:
        i = mid
        while i<=end:
            if i==end and list[i] == 0:
                return bin_search_sparsed_array(list, start, mid-1, value)
            elif list[i]!=0 and list[i] > value:
                print(" Start is ", start, " End is ", mid-1)
                return bin_search_sparsed_array(list, start, mid-1, value)
            elif list[i]!=0 and list[i] <= value:
                print("i = ",i, "end = ", end)
                return bin_search_sparsed_array(list,i, end, value)
            i+=1

# print("Length is ", len(list))
# print(" Index of 4 is ", bin_search_sparsed_array(list, 0, len(list)-1, 4))
print(" Index of 99 is ", bin_search_sparsed_array(list, 0, len(list)-1, 99))
            


























