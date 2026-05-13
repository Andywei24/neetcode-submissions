# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def to_array(head):
            arr = []
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next
            return arr
        arr1 = to_array(list1)
        arr2 = to_array(list2)
        res = arr1 + arr2
        res.sort()
        def to_linkedlist(arr):
            if not arr:
                return None
            
            head = ListNode(arr[0])
            curr = head
            for i in range(1, len(arr)):
                curr.next = ListNode(arr[i])
                curr = curr.next
            return head
        res = to_linkedlist(res)
        return res
