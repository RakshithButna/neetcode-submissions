class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     l, r =  0, 1  #default numbers
     maxP=0


     while r < len(prices):
        #profitable?
        if prices[l] < prices[r]:
            profits = prices[r] - prices[l]
            maxP = max(maxP , profits)

        else: 
            l = r # if l L is not small than r , then move L all the way to R
        r+=1
     return maxP     