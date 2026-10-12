# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next

        prev=None
        current=slow.next
        while current is not None:
            nextnode=current.next
            current.next=prev
            prev=current
            current = nextnode

        second=prev
        first =head
        while second is not None:
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
        # agsin reverse the second half to restore the original list
        #        p c
        # 1 2 3 x 3=2=1 
        current=prev
        prev=None
        while current is not None:
            nextnode=current.next  
            current.next=prev
            prev=current
            current = nextnode      
        return True