class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(0,n):
            ans.append(1)
        while sum(ans) != 0:
           if sum(ans) < 0:
               ans[0]+=1
           else:
               ans[0]-=1
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if ans[i] == ans[j]:
                    ans[0] -= 1
                    ans[j] += 1 
        return ans
