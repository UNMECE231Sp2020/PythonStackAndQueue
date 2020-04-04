# -*- coding: utf-8 -*-
"""
@author: Francisco Viramontes

Description:
    A python file that tests a local python class from stack.py
"""

import stack

if __name__ == "__main__":
    s1 = stack.Stack()
    s1.push(1)
    s1.push(5)
    
    s1.print_stack()