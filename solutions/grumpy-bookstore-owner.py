class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happyCust = sum([customers[x] for x in range(len(customers)) if grumpy[x]==0 ])
        
        print(happyCust)
        extraCust=sum([customers[x] for x in range(minutes) if grumpy[x]==1 ])
        res=extraCust
        for i in range(minutes,len(grumpy)):
            if(grumpy[i]==1):
                extraCust+=customers[i]
            elif(grumpy[i-minutes]==1):
                extraCust-=customers[i-minutes]
            res = max(res,extraCust)
        return res+happyCust