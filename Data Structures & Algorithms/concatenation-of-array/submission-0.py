class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range (len(nums)):
            temp.append(i)

        for i in range (len(temp)):
            nums.append(nums[i])

        return nums