'''
given a astring text， use the characters of text
to form as many instances of the word "balloon" as possible.

You can use each character in text at most once.
Return the maximum number of instances that can be formed.

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''


class Solution:
    def balloons(self, text: str) -> int:
        freq = {}

        target = 'balloon'
        target_set = set(target)

        for letter in text:
            if letter in target_set:
                freq[letter] = freq.get(letter, 0) + 1

        ans = 0
        while True:
            for char in target_set:
                freq[char] = freq.get(char, 0) - 2 if (char == 'l' or char == 'o') else freq.get(char, 0) - 1
                if freq[char] < 0:
                    return ans
            ans += 1




input = "nlaebolko"
sol = Solution()
res = sol.balloons(text = input)
print(res)