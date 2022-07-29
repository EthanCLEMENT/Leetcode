class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1
        begin = head
        while begin and begin.next:
            # if 1 == 1 then 1 = 2
            # 1 2 2
            # 1 2
            if begin.val == begin.next.val:
                begin.next = begin.next.next
            else:
                begin = begin.next
        return head

