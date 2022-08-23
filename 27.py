class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        while i < len(nums) and j >=0:
            if nums[j]==val:
                nums.pop()
                j -=1
            elif nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                i +=1
            else:
                i +=1
