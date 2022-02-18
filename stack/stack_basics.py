from collections import deque
# s = []
# s.append('https://cnn.com')
# s.append('https://google.com')
# s.append('https://webd.com')
# s.append('https://bbc.com')
# s.append('https://nepaltimes.com')
# s.append('https://nagarik.com')


class Stack:

    def __init__(self):
        self.container = deque()
        
    def push(self,value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)        


stack = deque()
# stack.pop() #! error cannot pop empty stack
# print(dir(stack)) #prints all the method available in a deque
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://cnn.com')
stack.append('https://google.com')
stack.append('https://webd.com')
stack.append('https://bbc.com')
stack.append('https://nepaltimes.com')
stack.append('https://nagarik.com')


# print(stack)
# stack.pop()
# print(stack)

#! Implementation from Stack class
s = Stack()
s.push('https://www.cnn.com/')
s.push('https://www.cnn.com/world')
s.push('https://cnn.com')
s.push('https://google.com')
s.push('https://webd.com')
s.push('https://bbc.com')
s.push('https://nepaltimes.com')
s.push('https://nagarik.com')
print(s.is_empty())
print(s.size())
s.pop()
print(s.is_empty())
print(s.size())