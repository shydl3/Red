class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # 按 Number of units inside each box of that type. 降序排序
        boxTypes.sort(key=lambda x: -x[1])
        curr_size = 0
        max_units = 0

        for num_of_box, units in boxTypes:
            # 尽可能装载units最多的箱子
            max_units += units * min(truckSize - curr_size, num_of_box)
            curr_size += min(truckSize - curr_size, num_of_box)

        return max_units