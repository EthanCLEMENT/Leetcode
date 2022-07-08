class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs)==0:
            return ans
        minlen = len(strs[0])
        for i in range(1,len(strs)):
            minlen = min(minlen, len(strs[i]))
        for i in range(0,minlen):
            curr = strs[0][i]
            print(curr)
            for j in range(0, len(strs)):
                if strs[j][i] != curr:
                    return ans
            ans +=curr
        return ans
            
            
            
