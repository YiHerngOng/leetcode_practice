import collections

class Solution(object):
	def subStringWithDistinctChar(self, s, k):
		s = list(s)

		def atMost(k):
			count = collections.defaultdict(int)

			left = 0
			ans = 0
			for right, x in enumerate(s):
				count[x] += 1
				while len(count) > k:
					count[s[left]] -= 1
					if count[s[left]] == 0:
						del count[s[left]]
					left += 1
				ans += right - left + 1
			return ans
		return atMost(k) - atMost(k-1)

s = Solution()
print s.subStringWithDistinctChar("pqpqs", 2)

