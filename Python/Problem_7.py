class Solution(object):
    def maxProfit(self, prices):
        prevprofit = 0
        buy = prices[0]
        sell = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                prevprofit = sell-buy if sell-buy > prevprofit else prevprofit
                buy = prices[i]
                sell = 0
            elif prices[i] > sell:
                sell = prices[i]

        profit = 0
        if prevprofit > sell - buy:
            if prevprofit > 0:
                profit = prevprofit
        elif sell-buy > 0:
            profit = sell-buy

        return profit

prices = [7,1,5,3,6,4]
obj = Solution()
obj.maxProfit(prices)