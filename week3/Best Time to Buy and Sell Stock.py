class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if prices == []:
            return 0
        buying_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buying_price:
                buying_price = prices[i]
            current_profit = prices[i] - buying_price
            if current_profit > profit:
                profit = current_profit

        return profit


