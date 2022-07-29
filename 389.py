class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)

        if len(s) < len(t):
            for x in s:
                t.remove(x)
            return(t[0])
        else:
            for x in t:
                s.remove(x)
            return(s[0])
