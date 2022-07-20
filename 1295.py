class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digit = str(i)
            if len(digit) % 2 == 0:
                count += 1
        return count
        
