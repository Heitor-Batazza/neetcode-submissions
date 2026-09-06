# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        if n == 1:
            curr2, prev2 = prev.next, None

            while curr2:
                tmp = curr2.next
                curr2.next = prev2
                prev2 = curr2
                curr2 = tmp

            return prev2

        else:
            tmp = prev
            for i in range(0, n-2):
                prev = prev.next
            if prev.next.next != None:
                prev.next = prev.next.next
            else:
                prev.next = None

            curr2, prev2 = tmp, None

            while curr2:
                tmp = curr2.next
                curr2.next = prev2
                prev2 = curr2
                curr2 = tmp
            return prev2

