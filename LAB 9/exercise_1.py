import random
import time
#---------------------------------------#      
# Implement Recursive selection sort here. 

# n: size of finalList - index is index of starting element

def recursive_selection_sort(data, data_len, index=0):
    # Set the base case 
    if (index == data_len - 1):
        return
    if not data:
        return
    # Find the minimum index 
    max_index = index
    for i in range(index + 1, data_len):
        if data[i] > data[max_index]:
            max_index = i
    # Swap the data 
    data[index], data[max_index] = data[max_index], data[index]
    # Recursively calling selection sort function 
    recursive_selection_sort(data, data_len, index + 1)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:  # Modified comparison for descending order
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def recurssive_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = recurssive_merge_sort(left_half)  # Recursively sort the left half
    right_half = recurssive_merge_sort(right_half)  # Recursively sort the right half

    return merge(left_half, right_half) # Merge the sorted halves


# Example usage:
my_list = [12, 45, 23, 78, 91, 54, 21]
print("Sorted list in descending order:", my_list)

#---------------------------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recurssive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recurssive_merge_sort(ascending_list)
    end_merge = time.time()

    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recurssive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))    



      

