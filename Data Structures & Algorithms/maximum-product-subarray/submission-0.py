class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = nums[0]
        curmin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curmax, curmin = curmin, curmax
            
            curmax = max(num, curmax * num)
            curmin = min(num, curmin * num)

            res = max(res, curmax)
        
        return res
