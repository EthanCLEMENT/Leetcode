class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        return [num for num in nums1 | nums2 | nums3 if (num in nums1) + (num in nums2) + (num in nums3) >= 2]
