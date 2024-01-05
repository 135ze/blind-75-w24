# 67. Add Binary
# Math, String, Bit Manipulation, Simulation

# Given two binary strings a and b, return their sum as a binary string.
# -----------------------------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)

        # add leading 0s
        if len_a < len_b:
            a = "0" * (len_b - len_a) + a
        else:
            b = "0" * (len_a - len_b) + b
        
        len_a = len(a) # update if a was shorter
        out = ""
        carry = 0
        # add from right to left with carry over if sum = 2, 3
        for i in range(0, len_a):
            cur_a = int(a[len_a - 1 - i])
            cur_b = int(b[len_a - 1 - i])
            cur_sum = cur_a + cur_b + carry
            if cur_sum == 0:
                out = '0' + out
                carry = 0
            elif cur_sum == 1:
                out = '1' + out
                carry = 0
            elif cur_sum == 2:
                out = '0' + out
                carry = 1
            else: # sum is 3
                out = '1' + out
                carry = 1
        # leftover carry value
        if carry:
            out = '1' + out
        return out
        
# -----------------------------------------------
# Testing
my_sol = Solution()

a = ["11", "1010"]
b = ["1", "1011"]

for i in range(2):
    print(my_sol.addBinary(a[i], b[i]))