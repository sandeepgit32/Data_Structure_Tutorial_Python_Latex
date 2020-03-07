from deque import Deque

def pal_checker(input_str):
    
    d = Deque()
    is_pal = True
    
    for ch in input_str:
        d.add_rear(ch)
    
    while d.size() > 1 and is_pal:
        first = d.remove_front()
        last = d.remove_rear()
        if first != last:
            is_pal = False
    
    return is_pal


print(pal_checker("technique"))
print(pal_checker("radar"))