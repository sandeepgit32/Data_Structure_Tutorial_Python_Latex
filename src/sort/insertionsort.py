def insertion_sort(input_list):
    
    for index in range(1, len(input_list)):
        current_value = input_list[index]
        pos = index
        
        while pos > 0 and input_list[pos - 1] > current_value:
            input_list[pos] = input_list[pos - 1]
            pos -= 1
        input_list[pos] = current_value
        
input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before sorting:")
print(input_list)
insertion_sort(input_list)
print("After insertion sort:")
print(input_list)