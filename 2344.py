class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        import functools, math
        nums.sort()
        x = functools.reduce(math.gcd, numsDivide)
        count = 0
        for num in nums:
            if x%num == 0:
                return count
            count+=1
        return -1  
