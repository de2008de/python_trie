class Node:
    def __init__(self, char: str):
        self.char = char
        self.next = dict()
        self.is_end = False

    def append_char(self, char: str):
        if char not in self.next:
            self.next[char] = Node(char)
        return self.next[char]

    def has_next(self, char: str):
        if char not in self.next:
            return False
        else:
            return self.next[char]


class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, s: str):
        if s[0] not in self.root:
            self.root[s[0]] = Node(s[0])
        prev = self.root[s[0]]
        for i in range(1, len(s)):
            prev = prev.append_char(s[i])
        prev.is_end = True

    def search(self, s: str):
        if s[0] not in self.root:
            return False
        prev = self.root[s[0]]

        for i in range(1, len(s)):
            prev = prev.has_next(s[i])
            if prev is False:
                return False
            if i == len(s) - 1:
                return prev.is_end
        return False

    def delete(self, s: str):
        if s[0] not in self.root:
            return
        prev = self.root[s[0]]
        list_node = [prev]

        for i in range(1, len(s)):
            prev = prev.has_next(s[i])
            list_node.append(prev)
            if prev is False:
                return
            if i == len(s) - 1 and prev.is_end is not True:
                return

        while len(list_node) != 0:
            last_node = list_node[-1]
            last_node.is_end = False
            if len(last_node.next) == 0:
                if len(list_node) > 1:
                    del list_node[-2].next[last_node.char]
                    del list_node[-1]
                else:
                    del self.root[last_node.char]
                    del list_node[-1]
            else:
                break
