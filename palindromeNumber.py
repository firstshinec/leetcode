class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            xtmp = x
            ytmp = 0
            if x // 10 < 0:
                return True
            else:
                while xtmp > 0:
                    ytmp = 10*ytmp + xtmp%10
                    xtmp = xtmp // 10
                if ytmp == x:
                    return True
                else:
                    return False