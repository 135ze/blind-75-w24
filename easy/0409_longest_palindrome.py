# 409. Longest Palindrome
# Hash Table, String, Greedy

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
# -----------------------------------------------
 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        length = 0
        singles = 0
        for c in s:
            if c in letters and letters[c] > 0:
                letters[c] -= 1
                singles -= 1
                length += 2 # add pair of letters
            else:
                letters[c] = 1
                singles += 1
        # add any single letter in middle of palindrome
        if singles > 0:
            length += 1
        return length
    # from sols -
    # alternative: use collections.Counter again
    #      odds = sum(v & 1 for v in collections.Counter(s).values())
    #      return len(s) - odds + bool(odds)
    
# -----------------------------------------------
# Testing
my_sol = Solution()

strings = ["abccccdd", "a"]

for i in range(2):
    print(my_sol.longestPalindrome(strings[i]))