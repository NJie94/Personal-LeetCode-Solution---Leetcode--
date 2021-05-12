class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        previous, result = 0,0
        search = {}

        for next in range(len(s)):
            if s[next] in search:
                previous = max(previous,search[s[next]]+1)
            search[s[next]] = next
            result = max(result,next-previous+1)
        return result
