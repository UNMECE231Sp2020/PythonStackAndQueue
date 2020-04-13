# -*- coding: utf-8 -*-
"""
@author: Francisco Viramontes

Description:
    A simple stack class
"""

#Syntax for creating a stack class
class Queue:
    #This doubles as a unparameterized default constructor and a parameterized
    #    default constructor
    def __init__(self, init_value=None):
        self.size_ = 0
        self.data_ = []
        if(init_value != None):
            self.data_.append(init_value)
        
    #Equivalent to overloading the << operator
    def __str__(self):
        #Cast data as a string
        str_temp = [ str(i) for i in self.data_ ]
        
        #Join it all into one string
        class_str = " ".join(str_temp)
        
        #Return string
        return class_str
            
    #Same as overloading == operator
    def __eq__(self, other):
        if(self.size() != other.size()):
            return False
        else:
            if(self.data_ == other.data_):
                return True
            else:
                return False
           
    #Same as overloading != operator
    def __ne__(self, other):
        if(self.size() != other.size()):
            return False
        else:
            if(self.data_ != other.data_):
                return True
            else:
                return False
        
    def size(self):
        return self.size_
    
    def front(self):
        return self.data_[-1]
    
    def back(self):
        return self.data[0]
    
    def enqueue(self, value):
        self.data_.insert(0, value)
        self.size_ += 1 #++ does not exist in python
    
    def dequeue(self):
        self.data_.pop(-1)
        self.size_ -= 1 #-- does not exist in python
    
    #print must be renamed print_stack because print is a keyword
    #however, this function is useless because of __str__
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
