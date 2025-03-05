class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)

        res=[0]*n
        code = code*2
        if k == 0:
            return res
        
        for i in range(len(res)):
            if k > 0:
                res[i] = sum(code[i + 1: i + k + 1])  # Sum next k elements
            else:
                res[i] = sum(code[i + n + k: i + n]) 
                
        return (res)
