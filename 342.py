class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isPowOfFour(n):
            if n == 1:
                return True
            elif n % 4 == 0 and n !=0:
                return isPowOfFour(n / 4)
            return False
        return isPowOfFour(n)
