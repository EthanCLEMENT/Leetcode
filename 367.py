class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        return num==math.isqrt(num)**2
