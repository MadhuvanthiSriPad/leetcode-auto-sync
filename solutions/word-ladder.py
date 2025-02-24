from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        hm= collections.defaultdict(list)
        wordSet = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neiWord = word[:i]+c+word[i+1:]
                    if neiWord in wordSet and neiWord!=word:
                        hm[word].append(neiWord)
        res=0

        q=hm[beginWord]
        print(q)
        while(q):
            for i in range(len(q)):
                neiW = q.popleft()
                

        