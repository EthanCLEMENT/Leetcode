class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(list(str(num)) )
        first = [num[0],num[2]]
        second = [num[1],num[3]]
        return int("".join(first)) + int("".join(second))
