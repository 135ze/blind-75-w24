from typing import List

# 704. Binary Search
# Array, Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# -----------------------------------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1
    
# -----------------------------------------------
# Testcases

my_sol = Solution()

nums = [[-1, 0, 3, 5, 9, 12], [-1, 0, 3, 5, 9, 12]]
targets = [4, -1]

for i in range (2):
    print(my_sol.search(nums[i], targets[i]))