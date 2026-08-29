class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        while len(queue) != 0:
            cur_w , level = queue.popleft()
            if cur_w == endWord:
                return level
            for i in range(0,len(cur_w)):
                for ch in "qwertyuiopasdfghjklzxcvbnm":
                    if ch == cur_w[i]:
                        continue
                    new_w = cur_w[:i] + ch + cur_w[i+1:]
                    if new_w in wordset:
                        queue.append((new_w,level + 1))
                        wordset.remove(new_w)
        return 0

        