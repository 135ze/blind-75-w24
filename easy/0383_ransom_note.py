# 383. Ransom Note
# Hash Table, String, Counting

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# -----------------------------------------------

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count available letters from magazine
        letters = {}
        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        # "use" letters in note
        for c in ransomNote:
            if c in letters:
                if letters[c] == 0: # all letters have been used
                    return False
                letters[c] -= 1
            else: # letter is not in magazine
                return False
        return True
    # from sols -
    # alternative: use collections.Counter
    #     return not collections.Counter(ransomNote) - collections.Counter(magazine)

# -----------------------------------------------
# Testcases
my_sol = Solution()

notes = ["a", "aa", "aa"]
magazines = ["b", "ab", "aab"]

for i in range(3):
    print(my_sol.canConstruct(notes[i], magazines[i]))
