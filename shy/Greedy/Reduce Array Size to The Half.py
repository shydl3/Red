'''
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.


Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
'''

from collections import Counter

# Counter统计元素的出现次数，并返回一个字典结构：
# eg Counter({'banana': 3, 'apple': 2, 'orange': 1})
# Counter({3: 3, 4: 2, 1: 1, 5: 1, 2: 1})
# 得到 {元素: 出现次数} 这样的字典。

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = Counter(arr)

        # counts.most_common() 返回一个 按出现频率降序排列的 (元素, 频率) 元组列表
        counts = [count for number, count in counts.most_common()]

        total_removed = 0
        ans = 0
        for count in counts:
            total_removed += count
            ans += 1
            if (total_removed >= len(arr)//2 ):
                break
        return ans