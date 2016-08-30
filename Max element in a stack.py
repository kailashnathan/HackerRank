# Enter your code here. Read input from STDIN. Print output to STDOUT
""" You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:46:24 2016

@author: Kailash Nathan
"""
class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)
    def maxitem(self):
        return max(self.items)
s=Stack()
n=int(input())
for i in range(0,n):
    x=input()
    h=(x.strip().split())
    if int(h[0])==1:
        if s.isEmpty():
            s.push(int(h[1]))
        else:
            s.push(max(s.peek(),int(h[1]))) #push the max element into the stack top
    if int(h[0])==2:
        s.pop()
    if int(h[0])==3:
        print(s.peek())
        
