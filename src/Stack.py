class Stack():
    
    # Constructor
    def __init__(self):
        self.items = []
        
    # Push item onto stack
    def push(self, item):
        self.items.append(item)				

    # Pop item from stack
    def pop(self):
        return self.items.pop()
    
    # Check whether the stack is empty or not
    def is_empty(self):
        return self.items == []
    
    # Peek at the topmost element of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    # Display the stack
    def display(self):
        #print(self.items[::-1])
        for i in self.items[::-1]:
            st = '| '+str(i)+' |'
            print(st)
            print('-'*len(st))
            
# Reversing a string using stack
def reverse_string(input_str):

    stack = Stack()
    for x in input_str:
        stack.push(x)

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

# Converting decimal --> binary a string using stack
def convert_binary(dec_num):
    
    '''
    Example : 242
    --------------
    242 / 2 = 121 -> 0
    121 / 2 = 60  -> 1
    60 / 2  = 30  -> 0
    30 / 2  = 15  -> 0
    15 / 2  = 7   -> 1
    7 / 2 = 3     -> 1
    3 / 2 = 1     -> 1
    1 / 2 = 0	  -> 1
    '''
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

# Checking the balancing and ordering of parentheses
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        elif paren in ")}]":
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

s = Stack()    

s.push(1)
s.push('A')
s.push(31)
s.push(4)
s.display()

print('Popped item =', s.pop())
s.display()
print('Reverse of \'Hello\' is', reverse_string("Hello"))
print('Binary of \'242\' is', convert_binary(242))
print('[a+b][c+d]:', is_paren_balanced("[a+b][c+d]")) 
print('[a+b][c+}d]:', is_paren_balanced("[a+b][c+}d]")) 
