class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        curr_max = 0
        for i in accounts:
            new_max = sum(i)
            if new_max > curr_max:
                curr_max = new_max
        return curr_max
