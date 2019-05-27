# https://leetcode-cn.com/problems/maximum-subarray/comments/
# Compare with the latter element, as long as the sum of former equence is larger than 0
        # the sequence can continue to extend. The minus inside the sequence does not influence the
        # result that the maximum sequence exists before it.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Solution 1
        maxsum = nums[0]
        sum_tmp = nums[0]
        
        for i in range(1, len(nums)):
            if sum_tmp > 0:
                sum_tmp += nums[i]
            else:
                sum_tmp = nums[i]
            maxsum = max(maxsum, sum_tmp)
        return maxsum
        
        # Solution 2
#         for i in range(1, len(nums)):
#             nums[i]= nums[i] + max(nums[i-1], 0)
#         print(nums)
#         return max(nums)
