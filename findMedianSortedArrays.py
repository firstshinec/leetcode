# Constuct a new arrary combining nums1 and nums2 in order, then it is easy to find the median.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        idx1 = 0
        idx2 = 0
        while 1:
            if len(nums1) == idx1 and len(nums2) == idx2:
                break
            else:
                if len(nums1) == idx1:
                    nums3 = nums3 + [nums2[idx2]]
                    idx2 += 1
                elif len(nums2) == idx2:
                    nums3 = nums3 + [nums1[idx1]]
                    idx1 += 1
                else:
                    if nums1[idx1] >= nums2[idx2]:
                        nums3 = nums3 + [nums2[idx2]]
                        idx2 += 1
                    else:
                        nums3 = nums3 + [nums1[idx1]]
                        idx1 += 1
        ListLen = len(nums3)
        if ListLen%2 == 0:
            median = (nums3[int(ListLen/2)]+nums3[int(ListLen/2-1)])/2
        else:
            median = nums3[int((ListLen+1)/2-1)]
        return median