class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        check = max(candies)
        res=[]

        for i in candies:
            if(i+extraCandies >=check):
                res.append(True)
            else:
                res.append(False)
        return res

        