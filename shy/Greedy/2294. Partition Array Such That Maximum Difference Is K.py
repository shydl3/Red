class Sulotion:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]

        # sort升序排序，从左到右依次比较，一旦与左边最小值的差值>k，则 计数+1，从当前位置重新开始排比
        for i in range(1, len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1

        return ans