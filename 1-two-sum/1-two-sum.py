class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enum = enumerate(nums)
        for i, num1 in enum:
            num2 = target - num1

            if num2 in nums[i+1:]:
                return [nums.index(num1), nums[i+1:].index(num2) + (i + 1)]