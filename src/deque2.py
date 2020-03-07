import collections 
  
# Initializing deque 
d = collections.deque([1,2,3]) 
print (d) 

# append() inserts element at right end  
d.append(4) 
print ('Insert 4 at right:', d) 
  
# appendleft() inserts element at left end  
d.appendleft(6) 
print ('Insert 6 at left:', d)

# pop() deletes element from right end  
d.pop() 
print ('Delete from right:', d)
  
# popleft() to deletes element from left end 
d.popleft() 
print ('Delete from right:', d)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
print('~'*40)
d = collections.deque([1, 2, 3, 3, 4, 2, 4]) 
print (d)

# index(element, beg, end) : This function returns the first index 
# of the value element, starting searching from beg till end index. 
print ("Number 4 first occurs at: {}".format(d.index(4, 2, 5))) 
  
# insert(i, a) insert the value i at index a
d.insert(4, 3) 
print ("After inserting 3 at 5th position: \n{}".format(d)) 
  
# count() counts the occurrences of 3 
print ("Count of 3 : {}".format(d.count(3))) 
  
# remove() removes the first occurrence of 3 
d.remove(3) 
print ("After deleting first occurrence of 3: \n{}".format(d)) 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('~'*40)
d = collections.deque([1, 2, 3,]) 
print(d)
# extend() to add multiple numbers to right end  
d.extend([4,5,6]) 
print ("The deque after extending deque at end: ") 
print (d) 
  
# extendleft() add multiple numbers to left end  
d.extendleft([7,8,9]) 
print ("The deque after extending deque at beginning: ") 
print (d) 
  
# rotate(n) to rotates the deque by n to the right 
d.rotate(-3) # rotates to the left by 3
  
# printing modified deque 
print ("The deque after rotating deque: ") 
print (d) 
