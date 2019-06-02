# https://leetcode-cn.com/problems/subsets

# Solution 1: add a new element to all the current subsets
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for i in range(len(nums)-1, -1, -1):
#             for subres in res[:]:
#                 res.append(subres+[nums[i]])
    
#         return res

# Solution2: backtracking
class Solution:
    def subsets(self, nums):
            tmp, ret = [], []
            self.dfs(self, nums, 0, tmp, ret)
            return ret

    def dfs(self, nums, index, tmp, ret):
        ret.append(tmp[:])
        if index >= len(nums):
            return
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.dfs(self, nums, i + 1, tmp, ret)
            tmp.pop()

a = Solution
b = a.subsets(a, [1, 2, 4])
print(b)