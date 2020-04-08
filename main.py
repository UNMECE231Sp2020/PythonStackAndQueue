# -*- coding: utf-8 -*-
"""
@author: Francisco Viramontes

Description:
    A python file that tests a local python class from stack.py
"""

#Formatted this way so that to call the stack call I don't have to type stack.Stack()
from stack import Stack
import queue

if __name__ == "__main__":
    s1 = Stack()
    s1.push(1)
    s1.push(5)
    
    s1.print_stack()
    print(s1)