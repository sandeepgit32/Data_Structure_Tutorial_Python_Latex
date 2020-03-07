def selection_sort(input_list):
    
    L = len(input_list)

    for i in range(L):        
        for j in range(i+1, L):
            min_idx = i
            if input_list[min_idx] > input_list[j]:
                min_idx = j
                swap_value_by_index(input_list, min_idx, i)
                
def swap_value_by_index(a_list, a, b):
    a_list[b], a_list[a] = a_list[a], a_list[b]

input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before sorting:")
print(input_list)
selection_sort(input_list)
print("After selection sort:")
print(input_list)
