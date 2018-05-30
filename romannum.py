# -*- coding: utf-8 -*-
"""
Spyder Editor
Byron Luo
Roman Numerals
"""

sym2num = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50,
           'XC':90, 'C':100, 'CD': 400, 'D':500, 'CM':900, 'M': 1000}

num2sym = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X',40:'XL', 50:'L',
           90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}


def to_roman(number):
    roman_num = ""
    for k,v in reversed(sym2num.items):
        pass
    while number >= sym2num['M']:
        roman_num = roman_num + num2sym[1000]
        number -= sym2num['M']
        
    while number >= sym2num['CM']:
        roman_num = roman_num + num2sym[900]
        number -= sym2num['CM']
        
    while number >= sym2num['D']:
        roman_num = roman_num + num2sym[500]
        number -= sym2num['D']   
        
    while number >= sym2num['CD']:
        roman_num = roman_num + num2sym[400]
        number -= sym2num['CD']
        
    while number >= sym2num['C']:
        roman_num = roman_num + num2sym[100]
        number -= sym2num['C']  
    
    while number >= sym2num['XC']:
        roman_num = roman_num + num2sym[90]
        number -= sym2num['XC']
        
    while number >= sym2num['L']:
        roman_num = roman_num + num2sym[50]
        number -= sym2num['L']   
        
    while number >= sym2num['XL']:
        roman_num = roman_num + num2sym[40]
        number -= sym2num['XL']
        
    while number >= sym2num['X']:
        roman_num = roman_num + num2sym[10]
        number -= sym2num['X']
        
    while number >= sym2num['IX']:
        roman_num = roman_num + num2sym[9]
        number -= sym2num['IX']   
        
    while number >= sym2num['V']:
        roman_num = roman_num + num2sym[5]
        number -= sym2num['V']
        
    while number >= sym2num['IV']:
        roman_num = roman_num + num2sym[4]
        number -= sym2num['IV']
        
    while number >= sym2num['I']:
        roman_num = roman_num + num2sym[1]
        number -= sym2num['I']
    return roman_num
    
print(to_roman(3549))