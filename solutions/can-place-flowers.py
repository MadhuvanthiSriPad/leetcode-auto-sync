class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        while (n):
            res=False
            for i in range (1,len(flowerbed)-1):
                if(flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0):
                    res=True
                    flowerbed[i]=1
            n-=1
                    
        return res
                    
        