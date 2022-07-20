class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = []
        for i in s:
            ans.append((i[::-1]))

        return ' '.join(ans)
        
