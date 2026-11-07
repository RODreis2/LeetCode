class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        atual = l1
        atual2 = l2
        texto1 = ""
        texto2 = ""
        while atual is not None:

            texto1 += str(atual.val) 
            
            atual = atual.next
            
        while atual2 is not None:

            texto2 += str(atual2.val) 
            
            atual2 = atual2.next

        sum = int(texto1) + int(texto2)
            
        print(sum)
l1 = ListNode(4,ListNode(2,ListNode(1)))
l2 = ListNode(6,ListNode(2,ListNode(7)))

Solution().addTwoNumbers(l1,l2)