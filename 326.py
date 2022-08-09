class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isPowOfThree(n):
            if n == 1:
                return True
            elif n % 3 == 0 and n !=0:
                return isPowOfThree(n / 3)
            return False
        return isPowOfThree(n)
