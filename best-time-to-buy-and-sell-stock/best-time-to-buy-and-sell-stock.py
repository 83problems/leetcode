class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        local = 0
        for i in range(len(prices)-1):
            local = max(0, local + prices[i+1] - prices[i])
            total = max(total, local)
        return total