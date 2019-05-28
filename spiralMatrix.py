# https://leetcode-cn.com/problems/spiral-matrix
# Use finite state machine to identify different direction. And set four values
# to limit the boundaries.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if matrix:
            tlist = [matrix[0][0]]
        else:
            return matrix
        urow = 0
        brow = len(matrix) - 1
        lcol = 0
        rcol = len(matrix[0]) - 1

        coord = [0, 0] #coordinate of current point
        i = 0 # state
        
        while 1:
            if i == 0:
                if coord[1] == rcol:
                    i = 1
                    urow += 1
                elif coord[1] < rcol:
                    coord[1] += 1
                    tlist.append(matrix[coord[0]][coord[1]])
                else:
                    break

            elif i == 1:
                if coord[0] == brow:
                    i = 2
                    rcol -= 1
                elif coord[0] < brow:
                    coord[0] += 1
                    tlist.append(matrix[coord[0]][coord[1]])
                else:
                    break

            elif i == 2:
                if coord[1] == lcol:
                    i = 3
                    brow -= 1
                elif coord[1] > lcol:
                    coord[1] -= 1
                    tlist.append(matrix[coord[0]][coord[1]])
                else:
                    break

            elif i == 3:
                if coord[0] == urow:
                    i = 0
                    lcol += 1
                elif coord[0] > urow:
                    coord[0] -= 1
                    tlist.append(matrix[coord[0]][coord[1]])
                else:
                    break
            if lcol > rcol or urow > brow: # check the cross of boundaries
                break
            # print(tlist)
            # print([coord[0], coord[1], i])
        return tlist