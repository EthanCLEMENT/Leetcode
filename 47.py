class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = nums.count(val)    
        for i in range(n):
            k = nums.index(val)
            nums.pop(k)   
     return len(nums)
