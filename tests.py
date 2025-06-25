import unittest
from lru import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_basic_operations(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)    # returns 1
        lru.put(3, 3)                      # evicts key 2
        self.assertEqual(lru.get(2), -1)   # returns -1 (not found)
        lru.put(4, 4)                      # evicts key 1
        self.assertEqual(lru.get(1), -1)   # returns -1 (not found)
        self.assertEqual(lru.get(3), 3)    # returns 3
        self.assertEqual(lru.get(4), 4)    # returns 4

    def test_update_existing_key(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(1, 10)                     # update key 1's value
        self.assertEqual(lru.get(1), 10)
        lru.put(3, 3)                      # evicts key 2
        self.assertEqual(lru.get(2), -1)

    def test_capacity_one(self):
        lru = LRUCache(1)
        lru.put(1, 1)
        self.assertEqual(lru.get(1), 1)
        lru.put(2, 2)                      # evicts key 1
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)

if __name__ == '__main__':
    unittest.main()
