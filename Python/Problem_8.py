class Solution(object):
    def maxProfit(self, prices):
        prevprofit = 0
        totalprofit = 0
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                # prevprofit = sell-buy if sell-buy > prevprofit else prevprofit
                buy = prices[i]
                totalprofit += prevprofit
                prevprofit = 0
            elif prices[i] >= buy:
                if (prices[i] - buy > prevprofit):
                    prevprofit = prices[i] - buy
                else:
                    totalprofit += prevprofit
                    prevprofit = 0
                    buy = prices[i]
            print(buy, prevprofit, totalprofit)
        if prevprofit > 0:
            totalprofit += prevprofit
        return totalprofit

prices = [1,2,4,2,5,7,2,4,9,0]
obj = Solution()
obj.maxProfit(prices)

