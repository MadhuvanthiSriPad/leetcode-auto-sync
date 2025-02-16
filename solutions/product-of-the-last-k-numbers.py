class ProductOfNumbers:

    def __init__(self):
        self.l = []

    def add(self, num: int) -> None:

        if num == 0:
            self.l = []  
        else:
            self.l.append(num)
        

    def getProduct(self, k: int) -> int:
        if k > len(self.l):
            return 0  
        product = 1
        for i in range(len(self.l) - k, len(self.l)):
            product *= self.l[i]
        return product

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)