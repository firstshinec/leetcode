# https://leetcode-cn.com/problems/spiral-matrix-ii

# refer to spiral-matrix, https://leetcode-cn.com/problems/spiral-matrix

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        urow = 0
        brow = len(matrix) - 1
        lcol = 0
        rcol = len(matrix[0]) - 1
        
        m = 1
        coord = [0, 0] #coordinate of current point
        i = 0 # state
        
        matrix[0][0] = 1
        while 1:
            if i == 0:
                if coord[1] == rcol:
                    i = 1
                    urow += 1
                elif coord[1] < rcol:
                    m += 1
                    coord[1] += 1
                    matrix[coord[0]][coord[1]] = m
                else:
                    break

            elif i == 1:
                if coord[0] == brow:
                    i = 2
                    rcol -= 1
                elif coord[0] < brow:
                    m += 1
                    coord[0] += 1
                    matrix[coord[0]][coord[1]] = m
                else:
                    break

            elif i == 2:
                if coord[1] == lcol:
                    i = 3
                    brow -= 1
                elif coord[1] > lcol:
                    m += 1
                    coord[1] -= 1
                    matrix[coord[0]][coord[1]] = m
                else:
                    break

            elif i == 3:
                if coord[0] == urow:
                    i = 0
                    lcol += 1
                elif coord[0] > urow:
                    m += 1
                    coord[0] -= 1
                    matrix[coord[0]][coord[1]] = m
                else:
                    break
            if lcol > rcol or urow > brow: # check the cross of boundaries
                break
        return matrix