class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        for i in range(len(nums)):
            first = nums[i]
            for j in range(len(nums)):
                second = nums[j]
                if j > i and (first + second) == target:
                    return i, j
                     