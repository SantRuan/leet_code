from math import remainder
from re import L
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

listNode1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))))
listNode2= ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None))))

# Melhor solução feita
class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(0, next=None)
        tail = dummy_head
        carry = 0
        while l1 or l2 or carry !=0 :
            _sum1 = l1.val if l1 is not None else 0
            _sum2 = l2.val if l2 is not None else 0
            
            sum = _sum1 + _sum2 + carry
            digit = sum % 10
            carry = sum // 10
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummy_head.next
        dummy_head.next = None
        return result
   
Solution.addTwoNumbers(l1=listNode1,l2=listNode2)