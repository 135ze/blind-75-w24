from typing import List

# 217. Contains Duplicate
# Array, Hash Table, Sorting

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# -----------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = True
        return False
    
# -----------------------------------------------
# Testing
my_sol = Solution()

nums = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

for i in range(3):
    print(my_sol.containsDuplicate(nums[i]))