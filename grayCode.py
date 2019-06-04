import copy
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        seq = [[0 for i in range(n)]] + [[0 for i in range(n-1)]+[1]]
        bit = n-1
        while 1:
            if bit == 0:
                dseq = self.convert2decimal(seq)
                return dseq
            else:
                nseq = copy.deepcopy(seq)
                for i in range(len(nseq)):
                    nseq[i][bit-1] = 1
                nseq.reverse()
                seq = seq + nseq
                bit -= 1

    def convert2decimal(self, seq):
        dseq = []
        for i in range(len(seq)):
            s = 0
            for j in range(len(seq[i])-1, -1, -1):
                s += seq[i][j]*2**(len(seq[i])-1-j)
            dseq.append(s)
        return dseq