class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        snums = sorted(nums)
        min_value = float("inf")
        sum_value = 0
        
        AIdx = 0
        while AIdx < len(nums) - 2:
            print("AIdx = " + str(AIdx))
            min_snums = snums[AIdx] + snums[AIdx+1] + snums[AIdx+2]
            max_snums = snums[AIdx] + snums[len(nums) - 2] + snums[len(nums) - 1]
            
            tmp = (min_snums - target)*(max_snums - target)
            if tmp > 0:
                if min_snums - target > 0:
                    min_value_tmp = min_snums - target
                    sum_value_tmp = min_snums
                else:
                    min_value_tmp = -(max_snums - target)
                    sum_value_tmp = max_snums
                if min_value_tmp < min_value:
                    min_value = min_value_tmp
                    sum_value = sum_value_tmp
                print("sum_value = " + str(sum_value))
            elif tmp == 0:
                min_value = 0
                sum_value = target
                return sum_value
            else:
                BIdx = AIdx + 1
                CIdx = AIdx + 2
                
                sum_value_tmp1 = 0
                sum_value_tmp2 = 0
                
                min_value_tmp1 = abs(snums[AIdx] + snums[BIdx] + snums[CIdx] - target)
                sum_value_tmp = snums[AIdx] + snums[BIdx] + snums[CIdx]
                if min_value_tmp1 == 0:
                    min_value = 0
                    sum_value = target
                    return sum_value
                    
                while CIdx <= len(nums) - 1:
                    if CIdx == len(nums) - 1 or snums[CIdx + 1] - snums[CIdx] > snums[BIdx + 1] - snums[BIdx]:
                        BIdx += 1
                    else:
                        CIdx += 1

                    min_value_tmp2 = abs(snums[AIdx] + snums[BIdx] + snums[CIdx] - target)
                    
                    if min_value_tmp2 < min_value_tmp1:
                        if min_value_tmp2 == 0:
                            min_value = 0
                            sum_value = target
                        return sum_value
                        min_value_tmp1 = min_value_tmp2
                        sum_value_tmp = snums[AIdx] + snums[BIdx] + snums[CIdx]
                    else:
                        min_value_tmp = min_value_tmp1
                        break

                if min_value_tmp < min_value:
                    min_value = min_value_tmp
                    sum_value = sum_value_tmp
            AIdx += 1
        return sum_value


###################
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        snums = sorted(nums)
        min_value = float("inf")
        sum_value = 0
        
        AIdx = 0
        while AIdx < len(nums) - 2:
            # print("AIdx = " + str(AIdx))
            min_snums = snums[AIdx] + snums[AIdx+1] + snums[AIdx+2]
            max_snums = snums[AIdx] + snums[len(nums) - 2] + snums[len(nums) - 1]
            
            tmp = (min_snums - target)*(max_snums - target)
            if tmp > 0:
                if min_snums - target > 0:
                    min_value_tmp = min_snums - target
                    sum_value_tmp = min_snums
                else:
                    min_value_tmp = -(max_snums - target)
                    sum_value_tmp = max_snums
                if min_value_tmp < min_value:
                    min_value = min_value_tmp
                    sum_value = sum_value_tmp
                # print("same sign, sum_value = " + str(sum_value))
            elif tmp == 0:
                min_value = 0
                sum_value = target
                return sum_value
            else:               
                for BIdx in range(AIdx+1, len(nums)-1):
                    min_sum1 = snums[AIdx] + snums[BIdx] + snums[BIdx + 1]
                    max_sum1 = snums[AIdx] + snums[BIdx] + snums[len(nums) - 1]
                    if (min_sum1 - target)*(max_sum1 - target) > 0:
                        if min_sum1 - target > 0:
                            min_value_tmp = abs(min_sum1 - target)
                            sum_value_tmp = min_sum1
                        elif min_sum1 - target < 0:
                            min_value_tmp = abs(max_sum1 - target)
                            sum_value_tmp = max_sum1
                        else:
                            min_value = 0
                            sum_value = target
                            return sum_value
                        if min_value_tmp < min_value:
                            min_value = min_value_tmp
                            sum_value = sum_value_tmp
                    else:
                        for CIdx in range(BIdx+1, len(nums)):
                            sum_value_tmp = snums[AIdx] + snums[BIdx] + snums[CIdx]
                            min_value_tmp = abs(sum_value_tmp - target)
                            if min_value_tmp < min_value:
                                min_value = min_value_tmp
                                sum_value = sum_value_tmp
            AIdx += 1
        return sum_value
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    