class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        m = n[::-1] 
        if n == m:
            return True
        
