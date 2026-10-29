class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # we need an array to store our final answers , Output is array , so this creates that and deafult is 1 

        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix # stores the current prefix product into the result array 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1): # the loop moves from right to left 
            res[i] *=postfix # we already have prefix result in res so we multiply each with postfix 
            postfix *= nums[i]
        return res
