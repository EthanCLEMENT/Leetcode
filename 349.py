class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums2=list(set(nums2))
        nums1=list(set(nums1))
        for i in nums1:
            if i in nums2:
                ans.append(i)
        return ans
