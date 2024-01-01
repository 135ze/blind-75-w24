# 125. Valid Palindrome
# Two Pointers, String

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# -----------------------------------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start <= end:
            # move pointers if not alphanumeric
            if not self.isAlphaNumeric(s[start]):
                start = start + 1
            elif not self.isAlphaNumeric(s[end]):
                end = end - 1
            else:
                # check if palindrome
                if s[start] != s[end]:
                    return False
                # move to next chars
                start = start + 1
                end = end - 1
        return True
    
    def isAlphaNumeric(self, c: str) -> bool:
         return ('a' <= c and c <= 'z') or \
                ('A' <= c and c <= 'Z') or \
                    ('0' <= c and c <= '9')

# -----------------------------------------------
# Testcases
my_sol = Solution()

strings = ["A man, a plan, a canal: Panama", "race a car", " "]

for string in strings:
    print(string, "is a palindrome: ", my_sol.isPalindrome(string))