class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for i in strs:
            word = ''.join(sorted(i))
            anagram[word].append(i)

        return list(anagram.values())