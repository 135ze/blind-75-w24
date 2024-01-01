# 242. Valid Anagram
# Hash Table, String, Sorting

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# -----------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # place all chars in s into dictionary
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1 # default val is 0
        
        # check all chars in t
        for c in t:
            if dict.get(c, 0) == 0: # default val is 0 for char not found
                return False
            else:
                dict[c] = dict.get(c) - 1
        
        # check for unused chars
        for c in dict:
            if dict.get(c) > 0:
                return False
        
        return True
    
# -----------------------------------------------
# Testcases
my_sol = Solution()

s = ["anagram", "rat"]
t = ["nagaram", "car"]

for i in range(2):
    print("is anagram: ", my_sol.isAnagram(s[i], t[i]))