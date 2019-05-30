# https://leetcode-cn.com/problems/rotate-list
# Extract the list value, rotate it and recreate a new ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        ListVal = []
        while head:
            ListVal.append(head.val)
            head = head.next
        ListLen = len(ListVal)
        if ListLen <= 1:
            return ListVal
        
        k = int(k % ListLen)
        
        NewListVal = ListVal[-k:] + ListVal[:-k]
        slist = ListNode(None)
        slist_tmp = slist

        for i in range(ListLen-1):
            slist_tmp.val = NewListVal[i]
            slist_tmp.next = ListNode(None)
            slist_tmp = slist_tmp.next
        slist_tmp.val = NewListVal[i+1]
        return slist
