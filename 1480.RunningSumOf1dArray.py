class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        for i in nums:
            count+=i
            ans.append(count)
        return ans
