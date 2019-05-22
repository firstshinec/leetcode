# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, compare the value of each ListNode at each round. Choose the minimum value to add on the new list
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = ListNode('')
        lt = l
        while any(lists):
            min_val = float('inf')
            min_idx = 0
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_idx = i
            lt.val = min_val
            lists[min_idx] = lists[min_idx].next
            
            if not any(lists):
                break
            lt.next = ListNode('')
            lt = lt.next
            
        return l

# Solution 2, similar to Solution 1 except the use of temporary list to peform stack operation
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = ListNode('')
        lt = l
        tlist = []
        ilist = []
        
        for i in range(len(lists)):
            if lists[i]:
                if not tlist:
                    tlist.append(lists[i].val)
                    ilist.append(i)
                else:
                    flag = 0
                    for j in range(len(tlist)):
                        if lists[i].val >= tlist[j]:
                            flag = 1
                            tlist.insert(j, lists[i].val)
                            ilist.insert(j, i)
                            break
                    if flag == 0:
                        tlist.append(lists[i].val)
                        ilist.append(i)
                        
        while tlist:
            min_val = tlist.pop()
            min_idx = ilist.pop()
            
            lt.val = min_val
            lists[min_idx] = lists[min_idx].next

            if lists[min_idx]:
                new_val = lists[min_idx].val
                if not tlist:
                    tlist.insert(0, new_val)
                    ilist.insert(0, min_idx)
                else:
                    flag = 0
                    for j in range(len(tlist)):
                        if new_val >= tlist[j]:
                            flag = 1
                            tlist.insert(j, new_val)
                            ilist.insert(j, min_idx)
                            break
                    if flag == 0:
                        tlist.append(new_val)
                        ilist.append(min_idx)
            if not tlist:
                break
            lt.next = ListNode('')
            lt = lt.next
        return l