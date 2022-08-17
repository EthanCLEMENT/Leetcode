class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        track = 1
        for i in nums:
            if i < 0:
                continue
            elif i == track:
                track += 1
                continue
        return track
