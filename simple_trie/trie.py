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
        self.root = Node('')

    def insert(self, s: str):
        if not self.root.has_next(s[0]):
            self.root.append_char(s[0])
        prev = self.root.next[s[0]]
        for i in range(1, len(s)):
            prev = prev.append_char(s[i])
        prev.is_end = True

    def search(self, s: str):
        if not self.root.has_next(s[0]):
            return False
        prev = self.root.next[s[0]]
        for i in range(1, len(s)):
            prev = prev.has_next(s[i])
            if prev is False:
                return False
            if i == len(s) - 1:
                return prev.is_end
        return False

    def get_prefix_string(self, prefix):
        if not self.root.has_next(prefix[0]):
            return False
        prev = self.root.next[prefix[0]]
        list_node = [prev]
        for i in range(1, len(prefix)):
            list_node.append(list_node[-1].has_next(prefix[i]))
            if list_node[-1] is False:
                break
        global_list_s = []
        self.get_all_strings_from(list_node[-1], '', global_list_s)
        results = []
        for s in global_list_s:
            results.append(prefix[:-1] + s)
        return results

    def get_all_strings_from(self, node: Node, temp_s, global_list_s):
        temp_s = temp_s + node.char
        if node.is_end:
            global_list_s.append(temp_s)
        for _, n in node.next.items():
            self.get_all_strings_from(n, temp_s, global_list_s)

    def delete(self, s: str):
        list_node = [self.root]
        for i in range(0, len(s)):
            list_node.append(list_node[-1].has_next(s[i]))
            if list_node[-1] is False:
                return
        if not list_node[-1].is_end:
            return
        else:
            list_node[-1].is_end = False
        while len(list_node) != 2:
            if len(list_node[-1].next) == 0:
                del list_node[-2].next[list_node[-1].char]
                del list_node[-1]
            else:
                break
