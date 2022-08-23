# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans=[]
        while head is not None:
            ans.append(head.val)
            head=head.next
        ans.sort()
        LL=ListNode()
        for i in ans[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
