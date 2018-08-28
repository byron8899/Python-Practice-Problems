# -*- coding: utf-8 -*-
"""
Byron Luo
Remove Element
"""


class Solution:
    
    def testFunction(self):
        print("Hello World")
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_list = [i for i in nums if i == val]
        return new_list
            
nums = [3,2,2,3]
val = 3

result = Solution()
print(result.removeElement(nums,val))