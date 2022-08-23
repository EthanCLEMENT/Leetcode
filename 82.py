# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        n=[]
        while head is not None:
            n.append(head.val)
            head=head.next
        seen=set()
        uniq=[]
        import collections
        ans=[item for item, count in collections.Counter(n).items() if count==1]
        LL=ListNode()
        for i in ans[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
