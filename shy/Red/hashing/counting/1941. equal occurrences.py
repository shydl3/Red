'''
given a string s, return True if all characters in s
have the same frequency of appearance
'''

from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        frequencies = counts.values()
        return len(set(frequencies)) == 1


# counter
from collections import Counter
class Solution2:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1

