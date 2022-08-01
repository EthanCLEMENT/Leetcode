class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        alpha = "abcedefghijklmnopqrstuvwxyz"
        s = s.lower()
        for i in s:
            if i.isdigit():
                ans += i
            if i in alpha:
                ans += i
        if ans == ans[::-1]:
            return True
        else:
            return False
