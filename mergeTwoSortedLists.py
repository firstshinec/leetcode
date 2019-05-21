# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# Be careful about the extension of listnode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode('')
        l3_tmp = l3
        l1_tmp = l1
        l2_tmp = l2
        
        while l1_tmp or l2_tmp:
            if l1_tmp and not l2_tmp:
                l3_tmp.val = l1_tmp.val
                l1_tmp = l1_tmp.next
            elif l2_tmp and not l1_tmp:
                l3_tmp.val = l2_tmp.val
                l2_tmp = l2_tmp.next
            else:
                if l1_tmp.val >= l2_tmp.val:
                    l3_tmp.val = l2_tmp.val
                    l2_tmp = l2_tmp.next
                else:
                    l3_tmp.val = l1_tmp.val
                    l1_tmp = l1_tmp.next
            if not (l1_tmp or l2_tmp):
                break
            l3_tmp.next = ListNode('')
            l3_tmp = l3_tmp.next
        return l3