# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        atual = head
        while atual is not None:
            head_list.append(atual.val)
            atual = atual.next
        print(head_list)

        if not head_list:     
            return None
    
        head_invertido = ListNode(head_list[-1])
        atual = head_invertido
        
        for i in range(-2, -len(head_list) - 1, -1):
            atual.next = ListNode(head_list[i])
            atual = atual.next
            
        return head_invertido
        