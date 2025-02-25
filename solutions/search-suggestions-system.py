from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary for storing child nodes
        self.suggestions = []  # Stores up to 3 lexicographically smallest words

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the Trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
            # Maintain at most 3 lexicographically smallest words
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def search_prefix(self, prefix: str) -> List[List[str]]:
        """Return suggestions for each prefix of the search word"""
        node = self.root
        result = []
        
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                # No more suggestions possible, fill remaining with empty lists
                while len(result) < len(prefix):
                    result.append([])
                break
        
        return result
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        # Insert sorted products to ensure lexicographical order
        for product in sorted(products):
            trie.insert(product)

        return trie.search_prefix(searchWord)