# https://leetcode-cn.com/problems/valid-parentheses/
# stack operation
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            else:
                if stack != [] and stack[-1] == s[i]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False