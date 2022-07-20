class Solution:
    def sortSentence(self, s: str) -> str:
        s = str.split(s)
        ans = []
        for i in range(len(s)):
            for j in range(0, len(s)-i-1):
                if s[j][-1] > s[j+1][-1]:
                   tmp = s[j]
                   s[j] = s[j+1]
                   s[j+1] = tmp   
        for i in s:
            ans.append(i[:-1])
        return ' '.join(ans)
