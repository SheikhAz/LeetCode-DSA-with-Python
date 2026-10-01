class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        def dfs(pos,curr,target):
            if target == 0:
                result.append(curr.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos , len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                dfs(i + 1 ,curr,target - candidates[i])
                curr.pop()
                prev = candidates[i]
        dfs(0,[],target)
        return result