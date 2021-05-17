'''
Theory on solving this problem
- Create a for loop to loop through a search of target-each of the id
- Then return the once the remain value after subtraction is found in the list of number
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #Create a Variable d with empty dictionary object
        d= {}

        #For each of i and id1 in the enums of nums 
        for i, id1 in enumerate(nums):
            if target - id1 in d:
                return [d[target - id1],i]
            d[id1] = i