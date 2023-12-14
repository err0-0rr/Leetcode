class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prt1=l1
        prt2=l2
        c=0
        node=ListNode()
        head=node
        pre=None
        while prt1!=None or prt2!=None:
            if prt1==None:
                val1=0
            else:
                val1=prt1.val
                prt1=prt1.next
            if prt2==None:
                val2=0
            else:
                val2=prt2.val
                prt2=prt2.next
            val=c+val1+val2
            rem=val%10
            c=val//10
            node.val=rem
            node.next=ListNode()
            pre=node
            node=node.next
        if c==0:
            pre.next=None
        else:
            node.val=c
        return head