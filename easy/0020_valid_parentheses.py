# 20. Valid Parentheses
# String, Stack

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# -----------------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # add opening brackets to stack
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            # check if it matches with stack top (or empty)https://discord.com/channels/@me/1109314151131648010
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            else:
                return False
        if stack: # unclosed brackets
            return False
        return True

# -----------------------------------------------
# Testcases
    
my_sol = Solution()

inputs = ["()", "()[]{}", "(]"]

for input in inputs:
    print("is valid: ", my_sol.isValid(input))