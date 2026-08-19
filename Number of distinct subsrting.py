class Node:
    def __init__(self):
        self.link = [None] * 26
    def containsKey(self,ch):
        return self.link[ord(ch)-ord('a')] is not None
    def put(self,ch,node):
        self.link[ord(ch)-ord('a')] = node
    def get(self,ch):
        return self.link[ord(ch)-ord('a')]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.cnt = 0
        self.node = self.root
        for ch in word:
            if not self.node.containsKey(ch):
                self.cnt += 1
                self.node.put(ch,Node())
            self.node = self.node.get(ch)
        
        return self.cnt+1

trie = Trie()
val = trie.insert("abab")
print(val)