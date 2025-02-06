'''
given a string s of lower and upper case English letters
A good string is a string which don't have two adjacent characters s[i] an s[i+1]
where
0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
'''
from Tools.scripts.pysource import print_debug

'''
Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
'''

'''
constraints:
1 <= s.length <= 100
s contains only lower and upper case English letters.
'''

# 1. use iteration.
# if two character's ASCII value difference == 32, they are a lowercase and uppercase pair, for English letters.
class Solution:
    def makeGreat(self, s: str) -> str:
        while len(s) > 1:
            find = False

            for i in range(len(s) - 1):
                curr_char, next_char = s[i], s[i+1]
                if abs(ord(curr_char) - ord(next_char)) == 32:
                    # 更新s，结束循环开始更新后的循环
                    s = s[:i] + s[i+2:]
                    find = True
                    break

            # 迭代多次后，直至find == False，代表查找完毕
            if not find:
                break

        return s

# recursion version:
    def makeGreat2(self, s: str) -> str:
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                return self.makeGreat2(s[:i]+s[i+2:])
        return s


# use stack；
    def makeGood(self, s: str) -> str:
        stack = []

        for curr_char in list(s):
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
            return ''.join(stack)