# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1 = ""
        string2 = ""

        while l1 or l2:
            if l1:
                string1 += str(l1.val)
                l1 = l1.next

            if l2:
                string2 += str(l2.val)  
                l2 = l2.next

        int1 = int(string1[::-1])
        int2 = int(string2[::-1])
        int3 = int1 + int2
        string3 = str(int3)
        
        print(string3)

        head = ListNode(int(string3[-1]))
        cur = head

        for i in range(len(string3) - 2, -1, -1):
            cur.next = ListNode(int(string3[i]))
            cur = cur.next

        return head








        