class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            for j in i:
                if j not in allowed:
                    count += 1
                    break
        ans=len(words) - count
        return ans
