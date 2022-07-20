class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        ans=set(Counter(s).values())
        return len(ans)==1
        
