# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l = lists[i]
                r = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(l, r)) 
            lists = mergedLists
        return lists[0]

    def mergeLists(self, l, r):
        dummy = ListNode(0)
        curr = dummy
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        if l:
            curr.next = l
        if r:
            curr.next = r
        return dummy.next
            
