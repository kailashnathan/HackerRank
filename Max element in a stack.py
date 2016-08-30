# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
          return self.items.pop()

     def prints(self):
          print self.items

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    

s=Stack()
m=Stack()
n=int(input())
maxi=0
for i in range (0,n):
     a=(raw_input())
     b=map(int,a.split())
     if b[0]==1:
          s.push(b[1])
          if m.size()==0:
               m.push(b[1])
          elif b[1]>m.peek():
               m.push(b[1])
     if b[0]==2:
          d=s.pop()
          if m.peek()==d:
               m.pop()
     if b[0]==3:
          x=m.peek()
          print x

