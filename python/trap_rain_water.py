class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        import numpy as np
        
        # left = [height[0]]
        left = np.zeros(len(height))
        left[0] = height[0]
        # right = [height[-1]]
        right = np.zeros(len(height))
        right[-1] = height[-1]
        
        for i in range(len(height)):
            # if i > 0:
            #     # left.append(max(height[:i+1]))
            #     left.append(max(height[i], left[i-1]))
            if i > 0:
                left[i] = max(height[i], left[i-1])  
                
        for j in range(len(height)):
            # if j < len(height) - 1:
                # right.append(max(height[j:]))
            # right.append(max(height[len(height)-2 - j], right[j]))
            # if j > 0:
            if j < len(height) - 1:
                right[-j-2] = max(height[-j-2], right[-j-1])

        # right.reverse()
        ans = 0
        
        for k in range(len(height)):
            ans += min(left[k], right[k]) - height[k]
        
        return int(ans)