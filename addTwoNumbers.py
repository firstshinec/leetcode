# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        lt = l3
        
        carry = 0
        while 1:
            if l1 != None or l2 != None:
                lv1 = l1.val if l1 != None else 0
                lv2 = l2.val if l2 != None else 0
                vt = lv1 + lv2 + carry
                if vt >= 10:
                    tmp = vt - 10
                    carry = 1
                else:
                    tmp = vt
                    carry = 0
                lt.next = ListNode(0)
                lt = lt.next
                lt.val = tmp
                
                l1 = l1.next if l1 != None else None
                l2 = l2.next if l2 != None else None
            else:
                if carry == 1:
                    lt.next = ListNode(1)
                    lt = lt.next
                break

        return l3.next