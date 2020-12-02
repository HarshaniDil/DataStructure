#Python Program to demostrate stack implementation
#Using queue module

from queue import LifoQueue

#Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of element in the stack
print(stack.qsize())

#push() function to push the elements to the stack
stack.put('a')
stack.put('b')
stack.put('c')

print(stack.qsize())
print(stack.full())
print(stack.empty())

#POP  from stack
print(stack.get())
print(stack.get())

print(stack.full())

stack.put('e')
print(stack.full())
print(stack.qsize())

stack.get()
stack.get()

print(stack.empty())