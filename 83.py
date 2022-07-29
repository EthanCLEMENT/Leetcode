class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        begin = head
        while begin and begin.next:
            if begin.val == begin.next.val:
                begin.next = begin.next.next
            else:
                begin = begin.next
        return head
