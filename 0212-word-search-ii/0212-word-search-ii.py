class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWORD = False
        self.refs = 0 # Optimization: Count how many words use this prefix

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWORD = True

    def removeWord(self, word):
        # Optimization: Remove word from Trie once found so we don't look for it again
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                prev = cur
                cur = cur.children[c]
                cur.refs -= 1
                if cur.refs == 0:
                    del prev.children[c]
                    return

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def DFS(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] not in node.children):
                return

            char = board[r][c]
            node = node.children[char]
            word += char
            
            if node.isWORD:
                res.append(word)
                node.isWORD = False # Mark as found
                root.removeWord(word) # Prune the Trie!

            # In-place marking to save memory
            board[r][c] = "#"
            
            # Standard DFS directions
            DFS(r + 1, c, node, word)
            DFS(r - 1, c, node, word)
            DFS(r, c + 1, node, word)
            DFS(r, c - 1, node, word)
            
            board[r][c] = char # Backtrack

        for r in range(ROWS):
            for c in range(COLS):
                DFS(r, c, root, "")

        return res