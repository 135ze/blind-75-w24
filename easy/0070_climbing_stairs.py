# 70. Climbing Stairs
# Math, DP, Memoization

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# -----------------------------------------------

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0] * (n + 1)
        # known
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            # add num ways to sum i - 1, then add a 1 with
            # num ways to sum to i - 2, then add a 2
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
# -----------------------------------------------
# Testcases
my_sol = Solution()

for i in range (1, 10):
    print(my_sol.climbStairs(i))