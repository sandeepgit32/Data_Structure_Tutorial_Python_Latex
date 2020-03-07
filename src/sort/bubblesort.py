def bubble_sort(input_list):
    
    L = len(input_list)
    for i in range(L): # Number of rounds
        for j in range(0, L-i-1):
            # Traverse the array from 0 to L-(i+1)
            # Last i elements are already in place
            if input_list[j] > input_list[j+1]:
                swap_value_by_index(input_list, j, j+1)

def swap_value_by_index(a_list, a, b):
    a_list[b], a_list[a] = a_list[a], a_list[b]

input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before sorting:")
print(input_list)
bubble_sort(input_list)
print("After bubble sort:")
print(input_list)
