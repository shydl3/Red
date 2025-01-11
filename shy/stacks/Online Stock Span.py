'''Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.'''


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1

        # 若当前price >= 栈顶price，不断弹出栈顶元素，直到当前price更小，则入栈
        # 确保stack递减
        while self.stack and self.stack[-1][0] <= price:
            # 要找到离当前price最近的更高price之间间距，
            # 触发弹出时说明当前price < 栈顶price，因此累加ans

            # 每个price会单独调用next()函数一次，因此ans不会累计，下一个price调用时，ans重新初始化为1
            # 因此每个入栈的数据相当于 price:对应的答案（离price最近的更高price之间间距）
            # 通过累加ans，相当于通过多段ans求和得到了完整的距离
            ans += self.stack.pop()[1]

        # 入栈数据格式是列表 [price, ans]
        # 第一个入栈的一定是第一个price，和初始化的ans=1
        self.stack.append([price, ans])

        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
