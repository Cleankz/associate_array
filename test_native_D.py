import unittest
from assoc_array import NativeDictionary

class MyTests(unittest.TestCase):

    def test_put(self):
        nd =  NativeDictionary(17)
        for i in range(17):
            nd.put(i,str(i))
        for i in range(17):
            self.assertIn(str(i),nd.slots)

    def test_get(self):
        nd =  NativeDictionary(17)
        self.assertEqual(None, nd.get("tyyjghj"))
        for i in range(17):
            nd.put(i,str(i))
        for i in range(17):
            self.assertIn(nd.get(i),nd.slots)

    def test_is_key(self):
        nd =  NativeDictionary(17)
        self.assertEqual(False, nd.is_key(1))
        for i in range(17):
            nd.put(i,str(i))
        for j in range(17):
            self.assertEqual(True,nd.is_key(j))
        self.assertEqual(False, nd.is_key(18))
if __name__ == '__main__':
    unittest.main()