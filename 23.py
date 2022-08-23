# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        ans=[]
        for i in lists:
            while i is not None:
                ans.append(i.val)
                i=i.next
        ans.sort()
        LL=ListNode()
        for i in ans[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
