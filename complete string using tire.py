class Node:
    def __init__(self):
        self.link = [None] * 26
        self.flag = False
    def containsKey(self,ch):
        return self.link[ord(ch)-ord('a')] is not None
    def put(self,ch,node):
        self.link[ord(ch)-ord('a')] = node
    def get(self,ch):
        return self.link[ord(ch)-ord('a')]
    def setEnd(self):
        self.flag = True
    def isEnd(self):
        return self.flag
    


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.node = self.root
        for ch in word:
            if not self.node.containsKey(ch):
                self.node.put(ch,Node())
            self.node = self.node.get(ch)
        self.node.setEnd()
        

    def checkIfPrefixExist(self, word: str) -> bool:
        fg = True
        self.node = self.root
        for ch in word:
            if not self.node.containsKey(ch):
                return False
            else:
                self.node = self.node.get(ch)
                if self.node.flag == False : return False
        
        return True
    
    
arr = ["n","ninja","ni","nin","ninj","ninga"]

trie = Trie()
for i in arr:
    trie.insert(i)

longest = ""

for i in arr:
    if trie.checkIfPrefixExist(i):
        if len(i) > len(longest):
            longest = i
        elif len(i) == len(longest) and i < longest:
            longest = i
print(longest)