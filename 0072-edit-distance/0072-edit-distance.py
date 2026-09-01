class Solution(object):
    def minDistance(self, word1, word2):
        w1 = len(word1)
        w2 = len(word2)
        cache = [[float('inf')]*(w2+1) for r in range(w1+1)]
        
        for j in range(w2+1):
            cache[w1][j] = w2 - j
        for i in range(w1+1):
            cache[i][w2] = w1 - i
        
        for i in range(w1-1,-1,-1):
            for j in range(w2-1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1])
        return cache[0][0]
        