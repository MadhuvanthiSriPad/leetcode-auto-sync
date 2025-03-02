class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hm={}
        res=""
        for i in strs:
            for j in i:
                hm[j]=hm.get(j,0)+1
        for key,val in hm.items():
            if(val==len(strs)):
                res+=key
            else:
                return res
        print(res)
        return res
