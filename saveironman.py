# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:27:12 2018

@author: byron
"""
'''
Jarvis is weak in computing palindromes for Alphanumeric characters.
While Ironman is busy fighting Thanos, he needs to activate sonic punch
but Jarvis is stuck in computing palindromes.
'''
# Task: Write a program that checks if the string is palindrome or not.

# function which return reverse of a string

def palindromes(string):
    newstring = ''
    # filter out the conjunctions,spaces, and symbols    
    for i in string:
        if i.isalpha() or i.isalnum():
            newstring +=i
    if newstring == newstring[::-1]:
        print('YES')
    else:
        print('NO')
testCase = input()

for t in range(int(testCase)):
    string =  [x for x in input().lower()]   
    palindromes(string)
