'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

Distinct 0-indexed integer arrays 的含义是：
数组中的所有元素是整数。
数组的索引从 0 开始。
数组中的元素是互不相同的，没有重复值。

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''

'''
Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
'''


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hashmap = {}

        for num in nums2:
            # 若当前元素始终>栈顶元素，弹出栈顶直到当前元素更小（或空栈）。再将当前元素入栈
            # 这样确保stack是递减排列
            while stack and num > stack[-1]:
                # 每次弹出的元素都比当前元素小，不断更新弹出元素指向当前元素的hashmap
                # 每个小于当前元素的，指向都会记录在hashmap
                hashmap[stack.pop()] = num
            # 当前元素入栈
            stack.append(num)

        # stack剩下的元素则表示没有比他们更大的。否则会在上一个for循环被弹出而加入hashmap
        # 因此统一标记为 -1
        while stack:
            hashmap[stack.pop()] = -1

        # 构建答案格式
        return [hashmap.get(i, -1) for i in nums1]

'''
Let n and m represent the length of the nums2 and nums1 array respectively.
Time complexity: O(n). The entire nums2 array (of size n) is scanned only once. 
Each of the stack's n elements are pushed and popped exactly once.

The nums1 array is also scanned only once. All together this requires O(n+n+m) time
Since nums1 must be a subset of nums2, we know m must be less than or equal to n. 
'''
