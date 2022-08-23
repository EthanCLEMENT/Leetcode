# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return None
        ans=''
        while head is not None:
            ans+=str(head.val)
            head=head.next
        ans=str(int(ans,base=2))
        return ans
