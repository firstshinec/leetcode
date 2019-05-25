class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = ['0']
        carry = 0
        
        if len(num1) == 1:
            if num1[0] == '0':
                return '0'
        if len(num2) == 1:
            if num2[0] == '0':
                return '0'
        
        for i in range(len(num2)):
            tmp2 = int(num2[-1-i])
            startTmp = i
            for j in range(len(num1)):
                startIdxTmp = -1-startTmp
                tmp1 = int(num1[-1-j])
                mtmp = tmp1*tmp2
                
                if startTmp > len(num) - 1:
                    num.insert(0, '0')
                    otmp = carry + mtmp
                else:
                    otmp = int(num[startIdxTmp]) + carry + mtmp
                
                num[startIdxTmp] = str(otmp%10)
                carry = otmp//10

                startTmp += 1
                # print('otmp = ' + str(otmp) + ', carry = '+ str(carry)+', mtmp = '+str(mtmp)+', num[start] = '+str(num[startIdxTmp]))
                # print(num)
            if carry > 0:
                num.insert(0, str(carry))
                carry = 0 #the carry should be reset, or it will be added once more
        num = ''.join(num)
        return num