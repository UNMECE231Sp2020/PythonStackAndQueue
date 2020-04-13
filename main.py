# -*- coding: utf-8 -*-
"""
@author: Francisco Viramontes

Description:
    A python file that tests a local python class from stack.py
"""

#Formatted this way so that to call the stack call I don't have to type stack.Stack()
from MyStack import Stack 
from MyQueue import Queue

s = Stack()
s.push(17)
s.push(12)
s.push(6)
print(s)

s.pop()
s.pop()
s.push(21)
print(s)

s2 = Stack(17)
s2.push(21)
print(s == s2)

s.push(12)
print(s, s.top())

print(s.search(44), s.search(21))


q = Queue(44)
q.enqueue(39)
q.enqueue(31)
q.enqueue(42)

print(q)
print(q.size(), q.back(), q.front())
q.dequeue()

q2 = Queue()
q2.enqueue(56)

print(q != q2)

q2.enqueue(67)
q2.print_queue()