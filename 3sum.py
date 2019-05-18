# https://leetcode-cn.com/problems/3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
# Sort the list in ascend order. Fix the first and the last index and use the bisection  to find the last one. It is hard to traverse all the cases.
#         SortedNums = sorted(nums)
#         AIdx = 0
#         CIdx = len(nums)-1
#         ThreeList = []
#         while AIdx < len(nums)-2:
#             if AIdx + 2 > CIdx:
#                 AIdx += 1
#                 CIdx = len(nums)-1
#                 continue
            
#             if AIdx > 0 and SortedNums[AIdx] == SortedNums[AIdx-1]:
#                 AIdx += 1
#                 continue
#             elif CIdx < len(nums)-1 and SortedNums[CIdx] == SortedNums[CIdx+1]:
#                 CIdx -= 1
#                 continue

#             Sum = SortedNums[AIdx] + SortedNums[CIdx]
#             if SortedNums[AIdx] + SortedNums[AIdx+1] + SortedNums[AIdx+2] > 0:
#                 break
#             elif SortedNums[AIdx] + SortedNums[len(nums)-2] + SortedNums[len(nums)-1] < 0:
#                 AIdx += 1
#                 CIdx = len(nums)-1
#                 continue
#             else:
#                 LeftIdx = AIdx
#                 RightIdx = CIdx
#                 while RightIdx >= LeftIdx:
#                     MidIdx = int((LeftIdx+RightIdx)//2)
#                     if MidIdx == LeftIdx:
#                         break
#                     # print(MidIdx)
#                     if SortedNums[MidIdx] < -Sum:
#                         LeftIdx = MidIdx
#                     elif SortedNums[MidIdx] > -Sum:
#                         RightIdx = MidIdx
#                     else:
#                         ThreeList = ThreeList + [[SortedNums[AIdx], SortedNums[MidIdx], SortedNums[CIdx]]]
#                         break
#                     if MidIdx == int((LeftIdx+RightIdx)//2):
#                         break
#                 CIdx -= 1
            
#         return ThreeList


# Sort the list in ascend order. Fix the first index and use the double indices to find the other two values meeting the total sum of 0.
        snums = sorted(nums)
        AIdx = 0
        ThreeList = []
        while AIdx < len(nums)-2:            
            if (snums[AIdx] + snums[AIdx+1] + snums[AIdx+2] > 0):
                break
            
            BIdx = AIdx + 1
            CIdx = len(nums) - 1
            
            while CIdx > BIdx:
                if snums[BIdx] + snums[CIdx] + snums[AIdx] > 0:
                    CIdx1 = CIdx - 1
                    while CIdx1 > BIdx:
                        if snums[CIdx1] == snums[CIdx]:
                            CIdx1 -= 1
                        else:
                            CIdx = CIdx1
                            break
                    if CIdx1 != CIdx:
                        break
                elif snums[BIdx] + snums[CIdx] + snums[AIdx] < 0:
                    BIdx1 = BIdx + 1
                    while CIdx > BIdx1:
                        if snums[BIdx1] == snums[BIdx]:
                            BIdx1 += 1
                        else:
                            BIdx = BIdx1
                            break
                    if BIdx1 != BIdx:
                        break
                else:
                    ThreeList = ThreeList + [[snums[AIdx], snums[BIdx], snums[CIdx]]]
                    BIdx1 = BIdx + 1
                    while CIdx > BIdx1:
                        if snums[BIdx1] == snums[BIdx]:
                            BIdx1 += 1
                        else:
                            BIdx = BIdx1
                            break
                    if BIdx1 != BIdx:
                        break
            AIdx1 = AIdx + 1
            while AIdx1 < len(nums)-2:
                if snums[AIdx1] == snums[AIdx]:
                    AIdx1 += 1
                else:
                    AIdx = AIdx1
                    break
            if AIdx1 != AIdx:
                break

        return ThreeList