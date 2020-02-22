#!/usr/bin/env python
# 3Sum-Series 

# 1. 3Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans_arr = []
        ans = []
        # table = {}
    
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + target == 0:
                    ans = [target, nums[start], nums[end]]
                    ans_arr.append(ans)
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                elif nums[start] + nums[end] + target < 0:
                    start += 1
                else:
                    end -= 1
        return sorted(ans_arr)


# 2. 3Sum Closest
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        diff = float("inf")
        ans = 0
        i = 0
        # for i in range(len(nums)):
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i-1]:
                first = nums[i]
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    curr_diff = (first + nums[start] + nums[end]) - target
                    if  abs(curr_diff) < diff:
                        ans = (first + nums[start] + nums[end])
                        diff = abs(curr_diff)
                    if curr_diff < 0:
                        start += 1
                    elif curr_diff >0:
                        end -= 1
                    else:
                        return target
            i += 1
        return ans

# 3 