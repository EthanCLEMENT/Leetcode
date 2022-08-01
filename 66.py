class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        digits = "".join(str(i) for i in digits)
        digits = eval(digits) + 1
        for i in str(digits):
            l.append(i)
        return l
