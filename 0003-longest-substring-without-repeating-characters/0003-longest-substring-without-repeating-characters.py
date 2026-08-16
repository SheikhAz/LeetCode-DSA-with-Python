class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        hashset = set()
        L = 0
        left = 0
        for right in range(n):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            L = max(L,right - left + 1)
        return L
        
        