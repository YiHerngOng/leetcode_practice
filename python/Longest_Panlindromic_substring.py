class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = 0
        
        ans = ""
        
        # define the start of longest substring
        start_of_longest = 0
        
        max_length = 1
        
        # two pointers for both ends of a string
        low = 0
        high = 0

        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        
        for p in range(1, len(s)):
            # search for even substring
            low = p-1
            high = p
            while low >= 0 and high<len(s) and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start_of_longest = low
                    max_length = high-low+1
                low -= 1
                high += 1

            # search for odd substring
            low = p - 1
            high = p + 1
            while low >= 0 and high<len(s) and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start_of_longest = low
                    max_length = high-low+1
                low -= 1
                high += 1
                
        

        return s[start_of_longest:start_of_longest+max_length]