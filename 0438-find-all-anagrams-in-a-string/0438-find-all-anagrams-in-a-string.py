class Solution(object):
    def findAnagrams(self, s, p):
        windowfreq = {}
        pfreq = {}
        for ch in p:
            pfreq[ch] = pfreq.get(ch,0)+1
        left = 0
        result = []
        for right in range(len(s)):
            ch = s[right]
            windowfreq[ch] = windowfreq.get(ch,0)+1
            if right - left + 1 > len(p):
                left_ch = s[left]
                windowfreq[left_ch] -= 1
                if windowfreq[left_ch]==0:
                    del windowfreq[left_ch]
                left += 1
            if windowfreq == pfreq:
                result.append(left)
        return result
        