class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=1:
            return n
        x=0
        sum1=0
        while n>=sum1:
            x+=1
            sum1+=x
        return x-1
    # LEET Code
    # Arrange the coins
    # Go down from the top adding one, when number is  less it goes together in the same line