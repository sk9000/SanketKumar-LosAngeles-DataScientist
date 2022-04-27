#!/usr/bin/env python
# coding: utf-8

# In[166]:


import unittest

def validity(ip):
    
    count=0
    
    for i in range(len(ip)):
        if ip[i].isnumeric()==False and ip[i]!='.':
            count+=1
            print("Invalid format")
            return
        
    for i in range(len(ip)-1):
        if ip[i]=='.' and ip[i+1]=='.':
            count+=1
            print("Invalid format")
            return
        
    if ip[0]=='.':
        count+=1
        print("Invalid: IP address cannot start with '.'")
        ip = ip[1:]
        
    if ip[-1]=='.':
        count+=1
        print("Invalid: IP address cannot end with '.'")
        ip = ip[:-1]
        
    lst = ip.split('.')
    
    if len(lst)!=4:
        count+=1
        print("Invalid: IP address should consist of 4 numbers separated by '.'")
    
    for i in range(len(lst)):
        if i==4:
            break
        if int(lst[i])<0 or int(lst[i])>255:
            count+=1
            print("Invalid: Value for segment", i+1, "should be between 0 and 255")
    
    if count==0:
        print("Valid IP address")
        for i in range(len(lst)):
            print("Segment", i+1, ":", lst[i], "; Length:", len(lst[i]))

class Test(unittest.TestCase):
    
    def test_1(self):
        actual = validity('12.12.12.12')
        expected = 'Valid IP address                    Segment 1 : 12 ; Length: 2                    Segment 2 : 12 ; Length: 2                    Segment 3 : 12 ; Length: 2                    Segment 4 : 12 ; Length: 2'
        self.assertEqual(actual, expected)
        
    def test_1(self):
        actual = validity('..12323')
        expected = 'Invalid format'
        self.assertEqual(actual, expected)
        
    def test_1(self):
        actual = validity('12.233.345.5676')
        expected = 'Invalid: Value for segment 3 should be between 0 and 255                    Invalid: Value for segment 4 should be between 0 and 255'
        self.assertEqual(actual, expected)
        
    def test_1(self):
        actual = validity('23.44.fff.vv')
        expected = 'Invalid format'
        self.assertEqual(actual, expected)

