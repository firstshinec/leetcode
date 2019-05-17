# https://leetcode-cn.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        i = 0
        
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        elif strs[0] == '':
            return ""
        else:
            charTmp = strs[0][0]
        while 1:
            for n in range(1, len(strs)):
                if i >= len(strs[n]):
                    return prefix
                if not (charTmp == strs[n][i]):
                    return prefix
            
            prefix = prefix + charTmp
            i += 1
            if i >= len(strs[0]):
                return prefix
            else:
                charTmp = strs[0][i]