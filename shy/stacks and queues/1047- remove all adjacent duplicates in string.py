'''
given a string s consisting of lowercase English letters
A duplicate removal consists of choosing two adjacent and equal letters and removing them

We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"

Example 2:
Input: s = "azxxzy"
Output: "ay"

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            # 模拟栈的列表 stack[-1] 访问的是最新添加进栈的元素
            # 如果当前元素==栈顶，代表相邻且重复，出栈。
            if stack and stack[-1] == c:
                stack.pop()
            else:
                # 否则代表不是重复元素，入栈，
                stack.append(c)

            # 通过stack储存每个元素，并在‘相邻且重复’时弹出。
            # 剩下的stack就是答案
            return ''.join(stack)
