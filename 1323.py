class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        new = list(num)
        for i in range(len(new)):
            print(new[i])
            if new[i] == '6':
                new[i] = '9'
                break
        return "".join(new)
