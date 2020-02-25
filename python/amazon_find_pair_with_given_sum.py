class Solution(object):
	def findPairGivenSum(self, nums, target):
		target -= 30

		p1 = 0
		ans = []
		hmap = {}

		for idx, x in enumerate(nums):
			complement = target - x
			if complement in hmap:
				if len(ans) > 0:
					temp = [x, complement]
					curr_ans = [nums[ans[0]], nums[ans[1]]]
					if max(temp) > max(curr_ans):
						ans = [hmap[complement], idx]
				else:
					ans = [hmap[complement], idx]
				# ans.append([hmap[complement], idx])
			hmap[x] = idx


		return ans

s =Solution()
print s.findPairGivenSum([50, 20, 40, 25, 30, 10], 90)



