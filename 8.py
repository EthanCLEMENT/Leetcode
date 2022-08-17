class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
            
        if len(s) == 0:
            return 0
        
        signs = 0
        for i in [0, min(1, len(s) - 1)]:
            if s[i] in "+-":
                signs += 1
        
        if signs > 1:
            return 0
        
        last_index = 0
        digits = 0
        for i in range(0 + signs, len(s)):

            if s[i] not in '0123456789':
                break
                
            digits += 1
            last_index = i
        
        if last_index == 0 and digits == 0:
            return 0
        
        return max( -2**31, min(int(s[0:last_index + 1]), 2**31-1) )
