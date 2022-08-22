class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        dp[1][0]=1
        dp[0][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        dp=dp[-1][-1]//2
        return dp
                
