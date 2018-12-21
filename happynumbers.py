# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:24:00 2018

@author: byron luo

A happy number is defined by the following process. 
1. Starting with any positive integer, replace the number by the sum 
of the squares of its digits.

2. Repeat the process until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1. 

3.Those numbers for which this process ends in 1 
are happy numbers, while those that do not end in 1 are unhappy numbers. 
Display an example of your output here. Find first 8 happy numbers.

"""

def check_happy_num(num):
    
    # Storing previous numbers in case the happy number doesn't exist 
    previous_num = []
    # Convert numbers into list of digits
    while(True):
        num = [int(x) for x in str(num)]
        
        # Summing Squaring digits
        num_square_digits = sum(list(map(lambda x: x**2, num)))
        
        if num_square_digits == 1:
            return True
        elif num_square_digits in previous_num:
            return False
        else:
            # Repeats it again
            num = num_square_digits
            previous_num.append(num)


num = int(input('Please enter a number: '))
happy_numbers = []
counter = 0
while(counter < 8):
    # Checks if happy number exists.  
    if check_happy_num(num):
        happy_numbers.append(num)
        counter = counter + 1
  
    num = num + 1
print(happy_numbers)
    