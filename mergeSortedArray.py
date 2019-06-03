# https://leetcode-cn.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums2):
            if i < j + m:
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    j += 1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            i += 1