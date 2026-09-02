class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if sum(nums)%k != 0:
            return False
        target = sum(nums)//k
        nums.sort(reverse = True)
        if nums[0] > target:
            return False
        
        used = [False]*len(nums)

        def backtrack(i,k,subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0,k-1,0)
            prev = -1
            for j in range(i,len(nums)):
                if used[j] or subsetSum + nums[j] > target or prev == nums[j]:
                    continue
                used[j] = True
                if backtrack(j + 1,k ,subsetSum + nums[j]):
                    return True
                used[j] = False
                prev = nums[j]
            return False
        return backtrack(0,k,0)

        