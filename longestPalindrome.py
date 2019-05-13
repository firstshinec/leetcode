class Solution:
    def longestPalindrome(self, s: str) -> str:
        MedIcr = 0
        MaxLen = 1
        MaxIdx = [0, 0]
        if len(s) <= 1:
            SubStr = s
        elif len(s) == 2:
            if s[0] == s[1]:
                SubStr = s
            else:
                SubStr = s[0]
        else:
            while 1:
                MedIcr += 1
                if MedIcr >= 2*len(s):
                    break
                if MedIcr % 2 == 1: # Even loopback seq
                    Med = MedIcr//2
                    MaxHalfPossLen = min(Med+1, len(s)-Med-1) # Find the length of maximum possible loopback sequence
                    # print(MaxHalfPossLen)
                    if 2*MaxHalfPossLen < MaxLen: # If the maximum LS has larger length than MaxHalfPossLen
                        continue
                    else:
                        if s[Med-(MaxLen-1)//2:Med+1] == s[Med+(MaxLen-1)//2+1:Med:-1]: # check if the internal seq meets the previous MaxLen
                            for n in range(MaxLen//2-1, MaxHalfPossLen):
                                if s[Med-n] == s[Med+n+1]:
                                    MaxLen = 2*(n+1)
                                    MaxIdx = [Med-n, Med+n+2]
                                else:
                                    break
                        else:
                            continue
                else: # Odd loopback seq
                    Med = MedIcr//2
                    MaxHalfPossLen = min(Med, len(s)-Med-1)
                    if 2*MaxHalfPossLen+1 < MaxLen: # If the maximum LS has larger length than MaxHalfPossLen
                        continue
                    else:
                        if s[Med-(MaxLen-1)//2:Med] == s[Med+(MaxLen-1)//2:Med:-1]:
                            for n in range(MaxLen//2, MaxHalfPossLen+1):
                                if s[Med-n] == s[Med+n]:
                                    MaxLen = 2*n + 1
                                    MaxIdx = [Med-n, Med+n+1]
                                else:
                                    break
                        else:
                            continue
            print(MaxIdx)
            SubStr = s[int(MaxIdx[0]):int(MaxIdx[1])]   
           
        return SubStr