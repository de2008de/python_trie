from .context import Trie

import unittest


class BasicTestSuite(unittest.TestCase):
    def test_insert(self):
        s = 'abc'
        trie = Trie()
        trie.insert(s)
        self.assertTrue(trie.search(s))

    def test_search(self):
        s1 = 'abc'
        s2 = 'cba'
        trie = Trie()
        trie.insert(s1)
        self.assertTrue(trie.search(s1))
        self.assertFalse(trie.search(s2))


if __name__ == '__main__':
    unittest.main()
