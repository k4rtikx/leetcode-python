# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        t1=l1
        t2=l2
        dummy=ListNode(-1)
        current=dummy 
        carry=0
        while( t1 is not None or t2 is not None ):
            summ=carry
            if t1 != None:
                summ+=t1.val
                t1=t1.next
            if t2 is not None:
                summ+=t2.val
                t2=t2.next
            newnode=ListNode(summ%10)
            carry= summ //10
            current.next=newnode
            current=current.next

        if carry != 0:
            newnode=ListNode(carry)
            current.next=newnode
        return dummy.next