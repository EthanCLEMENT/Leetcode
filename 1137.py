class Solution:
    dp = {}
    def tribonacci(self, n: int) -> int:
        if n ==0:
            return 0
        elif n <=2:
            return 1
        elif self.dp.get(n):
            return self.dp[n]
        self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.dp[n]
