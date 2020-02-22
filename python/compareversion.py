class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # return as follows: v1 > v2 => 1, v1 < v2 => -1, return 0 otherwise
        
        p = 0
        # p2 = 0
        version1 = [int(i) for i in version1.split(".") if i.isdigit()]
        version2 = [int(j) for j in version2.split(".") if j.isdigit()]
        
        if len(version1) > len(version2):
            n = len(version1)
        else:
            n = len(version2)
        
        while p < n:
            if len(version1) > len(version2):
                version2.append(0)
            else:
                version1.append(0)
                        
            if version1[p] > version2[p]:
                return 1
            elif version1[p] < version2[p]:
                return -1
            elif version1[p] == version2[p] and p == n-1: 
                return 0
            p+=1 