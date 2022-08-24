class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def isPowerOfTwo(n):
            if n == 1:
                return True
            elif n % 2 == 0 and n !=0:
                return isPowerOfTwo(n / 2)
            return False
        return isPowerOfTwo(n)
