class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")  # Use a set for O(1) lookup
        s = list(s)  # Convert to list for in-place modification
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]  # Swap vowels
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
        
        return "".join(s)  # Convert back to string