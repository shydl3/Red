'''
given a string s and an integer k,
find the length of the longest substring that contains at most k distinct characters
'''

# use sliding window, and hashing map to keep count of characters
from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)  # 存储当前窗口内字符的频率
    left = ans = 0  # 初始化窗口左边界和结果变量

    for right in range(len(s)):  # 遍历字符串的每个字符
        counts[s[right]] += 1  # 将当前字符加入窗口并更新计数

        # 当不同字符数量超过 k 时，收缩窗口
        while len(counts) > k:
            counts[s[left]] -= 1  # 左边字符计数减一

            if counts[s[left]] == 0:  # 如果该字符的计数为0，移出字典
                del counts[s[left]]

            left += 1  # 移动窗口左边界

        # 更新最大长度
        ans = max(ans, right - left + 1)

    return ans





