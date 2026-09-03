class Solution(object):
    def candy(self, ratings):
        can = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i - 1]:
                can[i] = 1 + can[i - 1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i + 1]:
                can[i] = max(can[i],1 + can[i+1])
        return sum(can)
        