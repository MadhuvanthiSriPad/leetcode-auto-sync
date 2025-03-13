class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0

        count = Counter(s)

        if all(val >= k for val in count.values()):
            return len(s)

        for ch in s:
            if count[ch] < k:
                # Split the string at this character and solve both parts
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))

        return len(s)