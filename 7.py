class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x:
            res = res * 10 + (x % 10)
            x //= 10
        
        if res > (2**31) - 1:
            return 0
        return int(res) * sign
