class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n=list(str(num))
        res=0
        for i in range(len(n)):
            s=n[i:i+k]
            kBeauty = int("".join(s))

            if(kBeauty>0 and num%kBeauty == 0 and len(s)==k):
                res+=1
        return res