class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def build_adj(wordList):
            hm=collections.defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    pattern = word[:i]+'*'+word[i+1:]
                    hm[pattern].append(word)
            return hm
        adj=build_adj([beginWord]+wordList)
        adj = build_adj([beginWord] + wordList)
        q = deque([[beginWord]])
        visited = set([beginWord])  # BeginWord should be in visited
        res = []
        found = False
        
        while q and not found:
            level_visited = set()
            level_len = len(q)

            for _ in range(level_len):  # Iterate over the current level
                path = q.popleft()
                word = path[-1]

                if word == endWord:
                    res.append(path)
                    found = True

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]

                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(path + [nei])  # Append new path correctly
                            level_visited.add(nei)

            visited.update(level_visited)  # Update visited at end of level

        return res