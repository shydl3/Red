'''
given an integer array arr, count how many elements x there are
such that x+1 also in arr
If there are duplicates in arr, count them separately.
'''

# loop over arr but do existence in hashset, to consider the duplicates.
class Solution:
    def countElements(self, arr: list[int]) -> int:
        has_set = set(arr)
        count = 0
        for i in arr:
            if i + 1 in has_set:
                count += 1

        return count



