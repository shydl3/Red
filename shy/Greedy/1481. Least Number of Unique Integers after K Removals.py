'''
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
'''

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        # Counter统计元素的出现次数，并返回一个字典结构：
        # eg Counter({'banana': 3, 'apple': 2, 'orange': 1})
        # Counter({3: 3, 4: 2, 1: 1, 5: 1, 2: 1})
        # 得到 {元素: 出现次数} 这样的字典。
        counts = Counter(arr)

        # counts.values()获取字典的所有值，reverse=True 按出现次数降序排序
        ordered = sorted(counts.values(), reverse=True)

        while k:
            # min_occurance为出现最少的次数.
            # k为限制移除k个元素
            min_occurance = ordered[-1]

            # 若最少出现次数小于k，直接全部移除
            # 思路是按出现次数从小到大，尽可能移除元素
            # 剩下的就是尽可能相同的元素
            if min_occurance <= k:
                k -= min_occurance
                ordered.pop()
            else:
                break

        return len(ordered)
