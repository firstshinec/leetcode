# https://leetcode-cn.com/problems/climbing-stairs/
# First, calculate the maximum number of 2-step. Then, traverse all the possible 2-step and
# adopt permuation to calculate the number of solutions

class Solution:
    def factorial(self, n: int):
        if n == 1 or n == 0:
            return 1
        elif n > 1:
            return n*self.factorial(n-1)
    def permuteC(self, m, n):
        return int(self.factorial(m)/(self.factorial(n) * self.factorial(m-n)))
    def climbStairs(self, n: int) -> int:
        num2 = n//2 #total 2-step
        t = 1
        for i in range(num2):
            # ts = n - 2*(i+1) + i+1 # calculate total steps (1-step and 2-step)
            t += self.permuteC(n-i-1, i+1)
        return t