from collections import deque

stack = deque()

#To push some elements in to the stack
stack.append('P')
stack.append('I')
stack.append('N')
stack.append('K')
stack.append('I')
print(stack)

#POP

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


print(stack)