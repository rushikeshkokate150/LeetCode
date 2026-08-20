class Node:
    def __init__(self):
        self.link = [None] * 2
    def containsKey(self,ch):
        return self.link[ch] is not None
    def put(self,ch,node):
        self.link[ch] = node
    def get(self,ch):
        return self.link[ch]

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(int(ch)):
                node.put(int(ch),Node())
            node = node.get(int(ch))
        

    def search(self, word):
        node = self.root
        string1 = ""
        for ch in word:
            if ch == '1':
                if node.get(0) != None:
                    string1 += '0'
                    node = node.get(0)
                else:
                    string1 += '1'
                    node = node.get(1)
            else:
                if node.get(1) != None:
                    string1 += '1'
                    node = node.get(1)
                else:
                    string1 += '0'
                    node = node.get(0)
        return string1
    
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for i in nums:
            word = format(i, '032b')
            # print(word)
            trie.insert(word)
        
        maxi = 0
        for i in nums:
            word = format(i, '032b')
            best = trie.search(word)
            val = i ^ int(best,2)
            maxi = max(maxi,val)
        return maxi
