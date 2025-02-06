'''
given an array of integers temperatures that represents the daily temp
return an array answer such that answer[i] is the number of days you have to
wait after the i th day to get a warmer temp.  If there is no future day that is warmer, have answer[i] = 0 instead.
'''

'''
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

'''
Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        # list 储存答案
        answer = [0] * n
        # 栈储存日期索引
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            # 若当前始终大于上次入栈的值：
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            # 否则入栈当前元素，即维持递减栈
            stack.append(curr_day)

        return answer