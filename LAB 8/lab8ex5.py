def binary_search1(key,theList,start,end):
 if start <= end:
        mid = (start + end) // 2 #gathering the middle index of the list
        if theList[mid] == key:  #position of the key is found
            return mid
        elif theList[mid] < key:
            return binary_search1(key, theList, mid + 1, end)
        else:
            return binary_search1(key, theList, start, mid - 1)
 else:
        return "Item is not in the list"

def main():
 some_list = [7,-2,1,3,5,7,9]
 print(binary_search1(9,some_list,0,len(some_list)-1))
 print(binary_search1(-8,some_list,0,len(some_list)-1))
 print(binary_search1(4,some_list,0,len(some_list)-1))
main()