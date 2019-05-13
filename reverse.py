# https://leetcode-cn.com/problems/reverse-integer
class Solution:
    def reverse(self, x: int) -> int:
        xtmp = x
        ytmp = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
            xtmp = -xtmp
        while xtmp > 0:
            ytmp = ytmp*10 + xtmp%10
            if float(ytmp) > 2**31-1 or float(ytmp) < -2**31:
                return 0
            xtmp = xtmp//10
        return sign*ytmp