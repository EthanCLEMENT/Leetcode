class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
       check = False
       if dividend < 0 or divisor < 0:
           check = True
       if dividend < 0 and divisor < 0:
           check = False
       ans = abs(dividend) // abs(divisor)
       if check:
           ans = -ans
       return min(max(-2147483648,ans),2147483647);   
