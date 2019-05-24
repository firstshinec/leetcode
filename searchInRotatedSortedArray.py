# https://leetcode-cn.com/problems/search-in-rotated-sorted-array

# Use bisection to search the target integer. The point is the condition to choose the next region in each iteration.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lidx = 0
        ridx = len(nums)-1
        midx = int((lidx+ridx)/2)
        
        if not nums:
            return -1
        if nums[lidx] == target:
            return lidx
        if nums[ridx] == target:
            return ridx
        
        while ridx > lidx:
            # print(midx)
            if nums[midx] == target:
                return midx
                
            if (nums[ridx] - target)*(nums[midx] - target) < 0:
                if (nums[lidx] - target)*(nums[midx] - target) < 0:
                    if abs(nums[lidx] - target) < abs(nums[ridx] - target):
                        ridx = midx
                    else:
                        lidx = midx
                else:
                    lidx = midx
            else:
                if (nums[lidx] - target)*(nums[midx] - target) < 0:
                    ridx = midx
                else:
                    if nums[midx] - target < 0:
                        if nums[midx] > nums[lidx]:
                            lidx = midx
                        else:
                            ridx = midx
                    else:
                        if nums[midx] < nums[ridx]:
                            ridx = midx
                        else:
                            lidx = midx
            midx = int((lidx+ridx)/2)
            if midx == lidx:
                break
        return -1
                    
            