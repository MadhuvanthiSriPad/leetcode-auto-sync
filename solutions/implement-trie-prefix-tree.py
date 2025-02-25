class Node:
    alph_size = 26

    def __init__(self):
        self.children = [None]*self.alph_size
        self.end_word = False
class Trie:

    def __init__(self):
        self.root = Node()

        

    def insert(self, word: str) -> None:

        node = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not node.children[index]:
                node.children[index]=Node()
            node = node.children[index]
        node.end_word = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.end_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)