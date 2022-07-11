class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 
                     'V': 5, 
                     'X': 10, 
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        ans = 0
        for i in range(len(s)-1,-1,-1):
            num = roman_map[s[i]]
            if 4*num < ans:
                ans-=num
            else:
                ans+=num
        return ans
                
        
