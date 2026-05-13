class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            goal = target - n
            if goal in hashMap:
                return [hashMap[goal], i]
            hashMap[n] = i


        