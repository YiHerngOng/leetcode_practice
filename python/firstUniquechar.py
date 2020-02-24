class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = d.get(s[i], 0) + 1
            else:
                d[s[i]] += 1
        
        unique_index = float("inf")
        for j in d.keys():
            if d[j] == 1:
                if s.index(j) < unique_index:
                    unique_index = s.index(j)
        
        if unique_index == float("inf"):
            unique_index = -1
        return int(unique_index)