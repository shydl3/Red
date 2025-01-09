'''
given an array of integers nums, find the max value of nums[i] + nums[j]
where nums[i] and nums[j] have the same digit sum (the sum of their individual digits)

Return -1 if there is no pair of numbers with the same digit sum.
'''


'''
identify a group by its digit sum
iterate through the array and group all the numbers with the same digit sum together in a hash map
Then we can iterate over that hash map and for each group with at least 2 elements, find the 2 max elements by sorting.
'''

from collections import defaultdict

# not efficient enough, could potentially cost up to O(n*logn) if every number in the input has the same digit sum.
# We can improve the time complexity and average space complexity by only saving the largest number seen so far for each digit sum
class Solution:
    def maxSum(self, nums: list[int]) -> int:

        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        dic = defaultdict(list)

        for num in nums:
            digit_sum = get_digit_sum(num)
            dic[digit_sum].append(num)

        ans = -1
        for key in dic:
            curr = dic[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])

        return ans


# more efficient way:
    def maxSum2(self, nums: list[int]) -> int:

        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        dic = defaultdict(int)
        ans = -1

        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dic:
                ans = max(ans, num + dic[digit_sum])
            dic[digit_sum] = max(num, dic[digit_sum])

        return ans