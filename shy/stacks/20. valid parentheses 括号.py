'''
有效括号
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
determine if the input string is valid

The string is valid if all open brackets are closed by the same type of closing bracket in the correct order,
and each closing bracket closes exactly one open bracket.

For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False

                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
        return not stack