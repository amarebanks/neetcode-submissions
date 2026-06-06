class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        length, MaxLen = 0, 0
        l, r = 0, 1

        while r < len(nums) + 1:
            if nums[l] == 1:
                length += 1
                l += 1
            else:
                l = r
                length = 0
            r += 1
            MaxLen = max(MaxLen, length)


        return MaxLen