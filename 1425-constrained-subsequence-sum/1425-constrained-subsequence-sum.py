class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        result = nums[0]
        max_heap = [(-nums[0],0)]

        for i in range(1,len(nums)):
            while i - max_heap[0][1] > k:
                heapq.heappop(max_heap)
            cur_sum = max(nums[i],nums[i] - max_heap[0][0])
            result  = max(result,cur_sum)
            heapq.heappush(max_heap,(-cur_sum,i))
        return result 