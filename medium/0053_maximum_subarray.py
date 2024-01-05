from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # calculate the sum of subarrays from 0 to each num
        acc_sum = [0]
        for num in nums:
            acc_sum.append(num + acc_sum[-1])
        acc_sum = acc_sum[1:] # discard dummy 0 from init

        max_acc = acc_sum[0] 
        max_sum = nums[0]
        print(acc_sum)
        for sum in acc_sum:
            print (sum, max_acc, max_sum)
            if sum > max_acc:
                max_sum = max(sum - max_acc, max_sum)
                max_acc = sum

        return max_sum

# -----------------------------------------------
# Testing
my_sol = Solution()

nums = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]

for arr in nums:
    print(my_sol.maxSubArray(arr))