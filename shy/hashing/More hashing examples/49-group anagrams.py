'''
given an array  of strings strs, group the anagrams together
给定一个字符串数组 strs，将字母重排组合在一起

For example, given strs = ["eat","tea","tan","ate","nat","bat"],
return
[["bat"],
["nat","tan"],
["ate","eat","tea"]].
'''


'''
The cleanest way to know if two strings are anagrams of each other is
by checking if they are equal after both being sorted
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # 在 defaultdict(list) 中：
        # 当一个键在字典中不存在时，defaultdict 会调用 list() 来为该键提供一个默认值（即一个空列表 []）
        # 因此访问一个不存在的键时，不会引发 KeyError
        groups = defaultdict(list)

        for s in strs:
            # ''.join() 将一个字符列表拼接成一个字符串
            # '连接符'.join(iterable)
            # '连接符'：定义每个元素之间的分隔符。
            # 如果不是用空字符串，而是用分隔符（例如 '-'），结果就会是 'a-e-t'，
            key = ''.join(sorted(s))

            #
            groups[key].append(s)

        # dictionary.values() doesn't actually return a list, but actually a view object.
        # We need to convert it to a list first.
        return list(groups.values())

'''

'''
