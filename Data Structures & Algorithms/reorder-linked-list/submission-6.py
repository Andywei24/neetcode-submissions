# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid to split the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # get the second portion and reverse 
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge
        l, r = head, prev
        while l and r:
            tmp1, tmp2 = l.next, r.next
            l.next = r
            r.next = tmp1
            l, r = tmp1, tmp2
