class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=1
        nums=list(set(nums))
        nums=sorted(nums)
        print(nums)
        for i in nums:
            if i==n:
                n+=1
            elif i<1:
                continue
            else:
                break
        return n
