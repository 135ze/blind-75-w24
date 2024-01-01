from typing import List

# 232. Implement Queue using Stacks
# Stack, Design Queue

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
# -----------------------------------------------

class MyQueue:
    stack1: List[int]
    stack2: List[int]

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # stack1 is a LIFO
        self.stack1.append(x) # push to top

    def pop(self) -> int:
        # move all elements from stack1 into stack2, resulting in reversed LIFO for stack2: FIFO
        while self.stack1: # not isEmpty
            self.stack2.append(self.stack1.pop())
        # grab first element from FIFO
        pop = self.stack2.pop()
        # move elements back into LIFO state in stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return pop

    def peek(self) -> int:
        # same logic as pop
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        pop = self.stack2[-1] # peek from top
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return pop
        
    def empty(self) -> bool:
        return not self.stack1

# -----------------------------------------------
# Testing
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()

push = [1, 2, 3, 4, 5]
for num in push:
    obj.push(num)

print (obj.stack2)
print(obj.stack1)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)