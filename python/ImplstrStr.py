class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(needle) > 0:
            if needle in haystack:                
                # return haystack.index(needle)
                i = 0
                j = 0
                # ans = 0
                while i < len(haystack):
                    if haystack[i] == needle[j]:
                        ans = i
                        while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                            i += 1
                            j += 1
                        if j == len(needle):
                            return ans
                        
                        i = ans + 1
                        j = 0
                        
                    else:
                        i += 1
            else:
                return -1
        else:
            return 0