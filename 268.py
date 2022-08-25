class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        for i in range(len(nums)):
            ans=i
            if nums[i]==0:
                continue
            if nums[i]!=i:
                return i
        return ans+1
