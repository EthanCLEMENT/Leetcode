# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if lis2 is None:
            return list1
        n=[]
        m=[]
        while list1 is not None:
            n.append(list1.val)
            list1=list1.next
        while list2 is not None:
            m.append(list2.val)
            list2=list2.next
        n+=m
        n.sort()
        LL=ListNode()
        for i in n[::-1]:
            newNode=ListNode(i)
            newNode.next=LL.next
            LL.next=newNode
        return LL.next
