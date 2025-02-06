'''
given an array of integers nums, and an integer k.
A continuous subarray is called 'nice' if there are k odd numbers in it
'''

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            # curr = 当前位置子数组奇数个数
            curr += num % 2

            # 当前位置，满足条件的子数组内奇数个数 curr - odds = k。 odds = curr - k
            # 更新ans，累加当前位置满足条件的这种数组个数 counts[odds]
            # 循环到最后一个元素就是答案
            ans += counts[curr -k]

            counts[curr] += 1

        return ans