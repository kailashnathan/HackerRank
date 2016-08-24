""" You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height."""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



n1,n2,n3 = map(int,input().strip().split(" "))

def inp():
    x=input()
    h1=(x.strip().split())
    
    return (h1)
x=inp()
y=inp()
z=inp()

def sum(x):
    x=x[::-1]
    q=[]
    
    j=0
    for i in x:
       j=j+int(i)
       q.append(j)
    #print(q)
    return (q)

a=sum(x)
b=sum(y)
c=sum(z)
f=0
def binarysearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found

if (n1<=n2) and (n1<=n3):
    for i in a:
        if (binarysearch(b,i)) and (binarysearch(c,i)):
            f=i
elif (n2<=n1) and (n2<=n3):
    for i in b:
        if binarysearch(a,i) and binarysearch(c,i):
            f=i
else:
    for i in c:
        if binarysearch(b,i) and binarysearch(a,i):
            f=i    
print(f)
