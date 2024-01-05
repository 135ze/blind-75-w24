from typing import List

# 169. Majority Element
# Array, Hash Table, Divide and Conquer, Sorting, Counting

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# -----------------------------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # my sol
        hashmap = {}
        maxElement = nums[0]
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1 # increase count
                curCount = hashmap[num]
                if curCount > len(nums) / 2: # at majority
                    return num 
                if curCount > hashmap[maxElement]: # update current greatest
                    maxElement = num 
            else:
                hashmap[num] = 1 # add to map
        return maxElement # should not be called
    
        # Just use default sort
        nums.sort()
        n = len(nums)
        return nums[n//2] # must be at this value because it's over majority
    
        # Moore Voting Algorithm
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0: # try another number, current isn't majority
                candidate = num
            
            if num == candidate:
                count += 1 # strengthen current number
            else:
                count -= 1 # weaken current num
        
        return candidate

# -----------------------------------------------
# Testing
my_sol = Solution()
nums = [[3, 2, 3], [2, 2, 1, 1, 1, 2, 2]]

for i in range(2):
    print(my_sol.majorityElement(nums[i]))