# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        ans=[]
        while head is not None:
            ans.append(head.val)
            head=head.next
        ans.reverse()
        for i in range(len(ans)):
            if i==n-1:
                ans.pop(i)
        ans.reverse()
        LL=ListNode()
        for i in ans[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
