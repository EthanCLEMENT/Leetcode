# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n=""
        m=""
        while l1 is not None:
            n+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            m+=str(l2.val)
            l2=l2.next
        ans=str(int(m)+int(n))
        LL=ListNode()
        for i in ans[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
