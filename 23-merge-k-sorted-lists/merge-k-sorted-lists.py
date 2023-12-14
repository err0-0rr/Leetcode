# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        head=ListNode()
        ptr=head
        while True:
            count=0
            mini=0
            val=10**5
            for i in range(n):
                if not lists[i]:
                    count+=1
                else:
                    if lists[i].val<=val:
                        val=lists[i].val
                        mini=i
            if count==n:
                break
            else:
                ptr.next=ListNode(val)
                ptr=ptr.next
                lists[mini]=lists[mini].next
        
        return head.next
                    
        