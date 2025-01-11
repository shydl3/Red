'''
given two strings s and t,
return True if they are equal when both are typed into empty text editors
'#' means a backspace character

For example, given s = "ab#c" and t = "ad#c", return true.
Because of the backspace 退格键, the strings are both equal to "ac".
'''
from http import HTTPStatus


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(strg):
            stack = []
            for c in strg:
                if c !='#':
                    stack.append()
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return build(s) == build(t)
