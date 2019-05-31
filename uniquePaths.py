# https://leetcode-cn.com/problems/unique-paths/
# Choose n-1 steps to move down from total m+n-2 steps.
# Then, adopt permutation formula and relative factorial

class Solution:
    def factorial(self, n: int):
        if n == 1 or n == 0:
            return 1
        elif n > 1:
            return n*self.factorial(n-1)
        
    def uniquePaths(self, m: int, n: int) -> int:
        t = m + n - 2
        return int(self.factorial(t)/(self.factorial(t-n+1)*self.factorial(n-1)))