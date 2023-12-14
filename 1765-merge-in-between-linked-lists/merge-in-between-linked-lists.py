# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        t=list1
        c=1
        while c!=a:
            t=t.next
            c+=1
        t1=t.next
        t.next=list2
        t2=list2
        while t2.next:
            t2=t2.next
        while c!=b:
            t1=t1.next
            c+=1
        t2.next=t1.next
        return list1