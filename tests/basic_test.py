from .context import Trie

import unittest


class BasicTestSuite(unittest.TestCase):
    def test_insert(self):
        s = 'abc'
        trie = Trie()
        trie.insert(s)
        self.assertTrue(trie.search(s))

    def test_multi_insert(self):
        s1 = 'abc'
        s2 = 'abd'
        s3 = 'ab'
        s4 = 'bbc'
        trie = Trie()
        trie.insert(s1)
        trie.insert(s2)
        trie.insert(s3)
        trie.insert(s4)
        self.assertTrue(trie.search(s1))
        self.assertTrue(trie.search(s2))
        self.assertTrue(trie.search(s3))
        self.assertTrue(trie.search(s4))

    def test_search(self):
        s1 = 'abc'
        s2 = 'cba'
        trie = Trie()
        trie.insert(s1)
        self.assertTrue(trie.search(s1))
        self.assertFalse(trie.search(s2))

    def test_delete(self):
        s1 = 'abc'
        s2 = 'abd'
        s3 = 'xyz'
        trie = Trie()
        trie.insert(s1)
        trie.insert(s2)
        trie.insert(s3)
        trie.delete(s1)
        self.assertFalse(trie.search(s1))
        self.assertTrue(trie.search(s2))
        self.assertTrue(trie.search(s3))
        trie.delete(s3)
        self.assertFalse(trie.search(s3))

    def test_get_prefix_string(self):
        s1 = 'abc'
        s2 = 'abcd'
        s3 = 'bcd'
        prefix1 = 'ab'
        prefix2 = 'xyz'
        prefix3 = 'bc'
        trie = Trie()
        trie.insert(s1)
        trie.insert(s2)
        trie.insert(s3)
        self.assertTrue(s1 in trie.get_strings_with_prefix(prefix1))
        self.assertTrue(s2 in trie.get_strings_with_prefix(prefix1))
        self.assertEqual(len(trie.get_strings_with_prefix(prefix1)), 2)

        self.assertTrue(s3 in trie.get_strings_with_prefix(prefix3))
        self.assertEqual(len(trie.get_strings_with_prefix(prefix3)), 1)

        self.assertEqual(trie.get_strings_with_prefix(prefix2), False)


if __name__ == '__main__':
    unittest.main()
