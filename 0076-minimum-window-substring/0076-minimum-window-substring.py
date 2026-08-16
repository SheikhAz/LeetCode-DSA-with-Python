class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""   
        window = {}
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c,0) + 1
        have = 0
        need = len(count_t)
        left = 0
        result = [-1,-1]
        reslen = float('inf')
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c ,0) + 1
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while need == have:
                if reslen > (right - left + 1):
                    result = [left,right]
                    reslen = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        l,r = result
        return s[l:r+1] if reslen != float('inf') else ""