class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        queue = deque([beginWord])
        parent = {beginWord :[]}
        found = False
        while queue and not found:
            seen = set()
            for i in range(len(queue)):
                word = queue.popleft()
                for i in range(0,len(word)):
                    for ch in "qwertyuiopasdfghjklzxcvbnm":
                        new_w = word[:i] + ch + word[i+1:]
                        if new_w in wordset:
                            if new_w not in parent:
                                parent[new_w] = [word] 
                                seen.add(new_w)
                                queue.append(new_w)
                            elif new_w in seen:
                                parent[new_w].append(word)
                            if new_w == endWord:
                                found = True
            wordset -= seen
        result = []
        def dfs(word,path):
            if beginWord == word:
                result.append(path[::-1])
                return
            for p in parent[word]:
                dfs(p,path+[p])
        if endWord in parent:
            dfs(endWord,[endWord])
        return result    

        