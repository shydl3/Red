'''
given a string s, find the longest substring without repeating characters

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        # stores the next index of current one
        # 所有最靠右的不重复元素 ：它的下一个index
        charToNextIndex = {}

        i = 0
        for j in range(n):
            # if found repeated element s[j], restrict the left side of sliding window, i
            # so that the window contains no repeating elements, and iteratively update the longest length
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans