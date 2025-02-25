class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hm= collections.defaultdict(list)
        wordSet = set(wordList)

        def build_adj_list(wordList):
            for word in wordList:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neiWord = word[:i]+c+word[i+1:]

                        if (neiWord in wordSet and neiWord!=word):
                            hm[word].append(neiWord)
            return hm

        adj_list = build_adj_list([beginWord]+ wordList)
        print(adj_list)
        
        q = deque([(beginWord,1)])
        visited=set()
        while(q):
            currWord , step = q.popleft()

            if currWord == endWord:
                return step
            for neiW in adj_list.get(currWord,[]):
                if neiW not in visited:
                    visited.add(neiW)
                    q.append((neiW,step+1))
        if endWord not in wordSet:
            return 0
        return step