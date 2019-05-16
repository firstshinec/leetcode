# https://leetcode-cn.com/problems/container-with-most-water
# Brute force searching has complexity O(n^2), exceeding the required time
# Double indices method: Initialize two indices in the first and the last sequence. Move the 
# index with lower height to find the possible larger area until two indices meet.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # MA = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         AreaTmp = min(height[i], height[j])*(j-i)
        #         if AreaTmp > MA:
        #             MA = AreaTmp
        # return MA
        
        # MA = 0
        # SortedIdx = sorted(range(len(height)), key=lambda k:height[k])
        # for i in range(len(height)-1):
        #     Tmp = SortedIdx[(i+1):]
        #     Tmp1 = Tmp
        #     for j in range(len(Tmp)):
        #         Tmp1[j] = abs(Tmp[j] - SortedIdx[i])
        #     AreaTmp = max(Tmp1)*height[int(SortedIdx[i])]
        #     if AreaTmp > MA:
        #         MA = AreaTmp
        # return MA
        
        # MA = 0
        # SortedIdx = sorted(range(len(height)), key=lambda k:height[k])
        # for i in range(len(height)-1):
        #     maxx = 0
        #     for j in range(i+1, len(height)):
        #         tmp = abs(SortedIdx[j]-SortedIdx[i])
        #         if tmp >= maxx:
        #             maxx = tmp
        #     AreaTmp = height[SortedIdx[i]] * maxx
        #     if AreaTmp > MA:
        #         MA = AreaTmp
        
        LeftIdx = 0
        RightIdx = len(height)-1
        
        MA = (RightIdx-LeftIdx)*min(height[LeftIdx], height[RightIdx])
        while RightIdx > LeftIdx:
            if height[RightIdx] >= height[LeftIdx]:
                AreaTmp = (RightIdx-LeftIdx)*height[LeftIdx]
                LeftIdx += 1
            else:
                AreaTmp = (RightIdx-LeftIdx)*height[RightIdx]
                RightIdx -= 1
            if AreaTmp > MA:
                MA = AreaTmp
        return MA