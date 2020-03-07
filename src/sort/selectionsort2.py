def selection_sort(input_list):
    
    L = len(input_list)
    Round_num = L-1
    Iterations_per_round = [L-x for  x in range(1, L)]
    
    for rnd in range(Round_num):
        for iteration in range(Iterations_per_round[rnd]):
            for i in range(iteration, L-1):
                if input_list[iteration] > input_list[i+1]:
                    swap_value_by_index(input_list, iteration, i+1)

def swap_value_by_index(a_list, a, b):
    a_list[b], a_list[a] = a_list[a], a_list[b]

input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before sorting:")
print(input_list)
selection_sort(input_list)
print("After selection sort:")
print(input_list)