from typing import List
# 53. Maximum Subarray
# Array, Divide and Conquer, DP

# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# -----------------------------------------------

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]
        for num in nums:
            # max sum from subarray with previous vs num
            cur_sum = max(num, cur_sum + num)
            # compare w previous
            max_sum = max(max_sum, cur_sum)
        return max_sum

        # divide and conquer from sols
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
        for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
        def maxSubArray(A, L, R):
            if L == R: return A[L]
            mid = (L + R) // 2
            return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
        return maxSubArray(nums, 0, len(nums)-1)
# -----------------------------------------------
# Testing
my_sol = Solution()

nums = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]

for arr in nums:
    print(my_sol.maxSubArray(arr))