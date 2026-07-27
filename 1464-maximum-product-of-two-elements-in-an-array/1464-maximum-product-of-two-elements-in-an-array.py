class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        big_one = 0
        big_two = 0

        for i in range(len(nums)):

            if nums[i] > big_one:
                big_two = big_one
                big_one = nums[i]
            elif nums[i] > big_two:
                big_two = nums[i]

        return (big_one-1) * (big_two-1)