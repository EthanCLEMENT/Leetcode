# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans=[]
        while head is not None:
            ans.append(head.val)
            head=head.next
        for i in range(0,len(ans)-1,2):
            ans[i],ans[i+1]=ans[i+1],ans[i]
        LL=ListNode()
        for i in ans[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
