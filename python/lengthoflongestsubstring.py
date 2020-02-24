class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = []
        substrings = []
        if len(s) == 0:
            return 0
        else:
            st = ""
            i = 0
            j = i
            curr_max = 0
            while (j < len(s)):
                if s[j] not in st:
                    st += s[j]
                    j += 1
                    curr_max = max(curr_max, len(st))
                else:
                    st = st.replace(st[0], "")
                
        return curr_max