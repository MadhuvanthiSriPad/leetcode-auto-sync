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
        q = deque([[beginWord]])
        visited = set()
        res = []
        found = False
        while q:
            level_visited = set()
            level_len = len(q)

            for i in range(level_len):
                path = q.popleft()
                word = path[-1]

                if word == endWord:
                    res.append(path)
                    found = True
                
                for i in range(len(word)):
                    pattern = word[:i]+'*'+word[i+1:]

                    for nei in adj[pattern]:
                        if nei not in visited:
                            new_path = path+[nei]
                            q.append(new_path)
                            level_visited.add(nei)
                if found:
                    break
            visited.update(level_visited)
        return res