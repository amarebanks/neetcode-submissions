import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        while True:
            maybe = random.choice(nums)
            if nums.count(maybe) > n // 2:
                return maybe 


        
