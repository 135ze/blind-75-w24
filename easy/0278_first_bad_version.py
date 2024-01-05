# 278. First Bad Version
# Binary Search, Interactive

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 1 # hard code for testing

# -----------------------------------------------

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # like binary search
        left, right = 1, n
        while right - left > 1:
            mid = (left + right) // 2
            #print(left, right, mid)
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid
            else:
                left = mid
        # when left and right are 1 apart
        if isBadVersion(left):
            return left
        else:
            return right


# -----------------------------------------------
# Testcases

my_sol = Solution()
print(my_sol.firstBadVersion(5))