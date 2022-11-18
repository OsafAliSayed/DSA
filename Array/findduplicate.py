# https://leetcode.com/problems/find-the-duplicate-number/submissions/

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]
            