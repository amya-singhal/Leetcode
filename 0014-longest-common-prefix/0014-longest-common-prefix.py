class Solution(object):
    def longestCommonPrefix(self, strs):    
        prefix = ""
        if (len(strs) == 1):
            return strs[0]
        if (len(strs) == 0):
            return ""
        for i in range (1, len(strs)):
            newprefix = ""
            minLength = min(len(strs[i]), len(strs[i-1]))
            for j in range(0, minLength):
                if strs[i][j] != strs[i-1][j]:
                    break
                newprefix = newprefix + strs[i][j]
            if newprefix == "":
                return ""
            else:
                if (i == 1):
                    prefix = newprefix
                prefix = min(newprefix, prefix)
        
        return prefix
            
            
        """
        :type strs: List[str]
        :rtype: str
        """
        