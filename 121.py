class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0]*len(prices)
        dp[0]=0
        for i in range(1,len(prices)):
            dp[i]=prices[i]-prices[i-1]
            if prices[i]>prices[i-1]:
                prices[i]=prices[i-1]
        return max(dp)
