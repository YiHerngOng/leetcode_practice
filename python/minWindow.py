class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0:
            return ""
        
        # left pointer and right pointer
        left = 0
        right = 0 
        
        # dict that contains T
        from collections import Counter
        dict_t = Counter(t) # dict that stores and makes each element's count as 1
        
        # dict of expandable window that keeps track of current word and counts 
        dict_window = {}
        
        # ans
        ans = float("inf"), left, right
        find_match = 0
        required_match = len(dict_t)
        
        while right < len(s):
            # check on right pointer 
            char = s[right]
            # store it in dict_window
            dict_window[char] = dict_window.get(char, 0) + 1
            
            # check if in dict_t
            if char in dict_t and dict_window[char] == dict_t[char]:
                find_match += 1 
            
            # if all elements in T are found, start reducing window size for minimization
            while left <= right and find_match == required_match:
                # check on left pointer
                char = s[left]
                # check current length and compare to the last
                if right - left + 1 < ans[0]:
                    ans = (right-left+1, left, right)
                
                # Contract window as do not include current left pointing char in the window
                dict_window[char] -= 1
                
                # check if current window still match the count in dict_t
                if char in dict_t and dict_window[char] < dict_t[char]:
                    find_match -= 1
                
                left += 1
                
            # move right window by 1
            right += 1
        
        if ans[0] == float("inf"):
            return ""
        else:
            return s[ans[1]: ans[2]+1]