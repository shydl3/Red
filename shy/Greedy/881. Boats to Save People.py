class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ans = 0

        # 双指针，j is last index
        i = 0
        j = len(people) - 1

        # ascending sort by default
        people.sort()

        while i <= j:
            # 如果最轻的人 + 最重的人 ≤ limit，则他们可以一起上船：
            # i += 1（轻的人上船）
            # j -= 1（重的人上船）
            if people[i] + people[j] <= limit:
                i += 1

            # 否则，最重的人单独上船：
            # j -= 1（重的人单独上船）
            j -= 1
            ans += 1
        return ans