'''
given an integer array cards, find the length of the shortest subarray that contains
at least one duplicate. if the array has no duplicates, return -1
'''
from multiprocessing.connection import default_family

'''
This question is equivalent to: 
what is the shortest distance between any two of the same element? 

For example, given cards = [1, 2, 6, 2, 1]
we would map 1: [0, 4], 2: [1, 3], and 6: [2]
Then we can iterate over the values and see that the minimum difference
'''

from collections import defaultdict

class Solution:
    def minCardPickup(self, cards: list[int]) -> int:
        dic = defaultdict(list)

        for i in range(len(cards)):
            dic[cards[i]].append(i)
            ans = float('inf')

            for key in dic:
                arr = dic[key]

                for i in range(len(arr) - 1):

                    # dist between 2 duplicate elements
                    ans = min(ans, arr[i + 1] - arr[i] + 1)

        return ans if ans < float('inf') else -1


# improved：
# only store the most recent index to update min dist
# improves the average space complexity
    def minCardPickup2(self, cards: list[int]) -> int:
        dic = defaultdict(list)
        ans = float('inf')

        for i in range(len(cards)):
            if cards[i] in dic:
                ans = min(ans, i - dic[cards[i]] + 1)
            dic[cards[i]] = i

        return ans if ans < float('inf') else -1