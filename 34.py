class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        if(nums.count(target)==0):
            return [-1,-1]
        ans.append(nums.index(target))
        for x in range(len(nums)-1,-1,-1):
            if(nums[x]== target ):
                ans.append(x)
                break

        return ans
