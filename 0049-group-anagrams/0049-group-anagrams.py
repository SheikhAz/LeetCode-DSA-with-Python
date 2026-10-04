from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for c in strs:
            count = [0]*26
            for s in c:
                count[ord(s) - ord("a")] += 1
            result[tuple(count)].append(c)
        return list(result.values())

