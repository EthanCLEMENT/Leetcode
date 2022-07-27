class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        inc = 0
        dec = len(s)
        ans = []
        for i in s:
            if i == 'I':
                ans.append(inc)
                inc += 1
            else:
                ans.append(dec)
                dec -= 1
        ans.append(dec)
        return ans 
