# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None:    # handle 3 error 
            return None
        if head.next is None:
            head = None
            return head
        if head.next.next is None:
            head.next = None
            tail = head
            return head

        slow=head
        fast=head
        fast=fast.next.next  # skiping the 1 term so that i point exactly where i have to point 
        while fast is not None and fast.next is not None: # even fast reaches None and in odd fast reaches at last so fast.next is None 
            fast=fast.next.next
            slow= slow.next
        slow.next=slow.next.next
        return head