class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            currP = prices[r] - prices[l]
            if prices[r] > prices[l]:
                    profit = max(currP, profit)
            else:
                l = r
            r += 1
        return profit