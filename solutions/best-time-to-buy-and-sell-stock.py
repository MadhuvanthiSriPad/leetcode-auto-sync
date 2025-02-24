class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof,min_price = -float('inf'),float('inf')

        for i in prices:
            min_price = min(min_price,i)
            max_prof = max(max_prof,i-min_price)
        return max_prof

