class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.frequency = 0   # track word frequency


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
        node.frequency += 1

    def searchPrefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def getWords(self, node, prefix, result):
        if node.isEnd:
            result.append((prefix, node.frequency))

        for ch in node.children:
            self.getWords(node.children[ch], prefix + ch, result)

    def autocomplete(self, prefix):
        node = self.searchPrefix(prefix)
        if not node:
            return []

        result = []
        self.getWords(node, prefix, result)

        # sort by frequency (highest first)
        result.sort(key=lambda x: x[1], reverse=True)

        # return top 5 words only
        return [word for word, freq in result[:5]]


# ----------- TESTING -----------
if __name__ == "__main__":
    trie = Trie()

    words = ["apple", "app", "application", "app", "apple", "apex"]
    for word in words:
        trie.insert(word)

    print(trie.autocomplete("app"))
