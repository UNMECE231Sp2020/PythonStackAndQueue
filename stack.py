# -*- coding: utf-8 -*-
"""
@author: Francisco Viramontes

Description:
    A simple stack class
"""

#Syntax for creating a stack class
class Stack:
    #This doubles as a unparameterized default constructor and a parameterized
    #    default constructor
    def __init__(self, init_value=None):
        self.size_ = 0
        self.data_ = []
        if(init_value != None):
            self.data_.append(init_value)
        
    def size(self):
        return self.size_
    
    def top(self):
        return self.data_[-1]
    
    def push(self, value):
        self.data_.append(value)
        self.size_ += 1 #++ does not exist in python
    
    def pop(self):
        self.data_.pop(-1)
        self.size_ -= 1 #-- does not exist in python
    
    #print must be renamed print_stack because print is a keyword
    def print_stack(self):
        for item in self.data_:
            print(item, end=" ")
            #end=" " means that each print will end with a space instead of a
            #    new line
            
    def search(self, value):
        for item in self.data_:
            if(item == value):
                return True
        return False
    
    #TODO: =, ==, !=, <<, empty