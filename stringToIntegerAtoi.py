# https://leetcode-cn.com/problems/string-to-integer-atoi
class Solution:
    def myAtoi(self, s: str) -> int:
        Idx = 0
        Status = 0 # 0: check the first valid character, 1: count the continuous integer
        tmp = 0
        sign = 1
        while Idx < len(s):
            if Status == 0:
                if s[Idx] == ' ':
                    Idx += 1
                elif s[Idx] == '-':
                    sign = -1
                    Status = 1
                    Idx += 1
                elif s[Idx] == '+':
                    Status = 1
                    Idx += 1
                elif ord(s[Idx]) >= 48 and ord(s[Idx]) <= 57:
                    Status = 1
                    tmp = int(s[Idx])
                    Idx += 1
                else:
                    tmp = 0
                    break
            elif Status == 1:
                if ord(s[Idx]) >= 48 and ord(s[Idx]) <= 57:
                    ftmp = float(tmp*10 + int(s[Idx]))
                    if sign > 0 and ftmp > 2**31 - 1:
                        return (2**31 - 1)
                    elif sign < 0 and ftmp > 2**31:
                        return (-2**31)
                    else:
                        tmp = tmp*10 + int(s[Idx])
                        Idx += 1
                else:
                    break
            else:
                break
        return sign*tmp