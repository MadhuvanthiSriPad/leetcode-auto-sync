class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)
        for ch in strs:
            char_count = [0]*26       

            for c in ch:
                char_count[ord(c)-ord('a')]+=1

            combo = tuple(char_count)

            anagram[combo].append(ch)
        return list(anagram.values())
