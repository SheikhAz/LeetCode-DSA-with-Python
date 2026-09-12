class Solution(object):
    def shortestSubarray(self, nums, k):
        result = float('inf')
        cur_sum = 0
        q = collections.deque()

        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum >= k:
                result = min(result,i+1)
            while q and cur_sum - q[0][0] >= k:
                prefix , end_idx = q.popleft()
                result = min(result,i - end_idx)

            while q and q[-1][0] > cur_sum:
                q.pop()
            q.append((cur_sum , i))
        return -1 if result == float('inf') else result

        