class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        res = float('inf')
        for i in range(len(blocks)-k+1):
            white = 0
            for j in range(i,i+k):
                if(blocks[j]=='W'):
                    white +=1
            if(white == 0):
                return 0
            res = min(res,white)
        return res