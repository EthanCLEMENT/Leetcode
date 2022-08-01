# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # 5 -> 4 -> 3 -> 2 -> 1 -> None
        
        previous = None  # previous initially points to None
        current = head # current points at the first element
        
        # go till the last element of the list
        while current is not None:
            next = current.next # following points at the second element
            current.next = previous # reverse the link
            previous = current # move previous one step ahead
            current = next # move current one step ahead

        head = previous
        return head
