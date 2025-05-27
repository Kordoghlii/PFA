import unittest
from queue_utils import *

class TestQueueUtils(unittest.TestCase):
    def test_enqueue(self):
        queue = []
        self.assertEqual(enqueue(queue, 1), [1])
        self.assertEqual(enqueue(queue, 2), [1, 2])

    def test_dequeue(self):
        queue = [1, 2, 3]
        self.assertEqual(dequeue(queue), 1)
        self.assertEqual(queue, [2, 3])
        self.assertIsNone(dequeue([]))

    def test_peek(self):
        self.assertEqual(peek([1, 2, 3]), 1)
        self.assertIsNone(peek([]))

    def test_is_empty(self):
        self.assertTrue(is_empty([]))
        self.assertFalse(is_empty([1, 2]))

    def test_queue_size(self):
        self.assertEqual(queue_size([1, 2, 3]), 3)
        self.assertEqual(queue_size([]), 0)

    def test_clear_queue(self):
        queue = [1, 2, 3]
        self.assertEqual(clear_queue(queue), [])
        self.assertEqual(queue, [])

    def test_copy_queue(self):
        queue = [1, 2, 3]
        copy = copy_queue(queue)
        self.assertEqual(copy, [1, 2, 3])
        copy.append(4)
        self.assertEqual(queue, [1, 2, 3])

    def test_reverse_queue(self):
        self.assertEqual(reverse_queue([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_queue([]), [])

    def test_contains_item(self):
        self.assertTrue(contains_item([1, 2, 3], 2))
        self.assertFalse(contains_item([1, 2, 3], 4))

    def test_merge_queues(self):
        self.assertEqual(merge_queues([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_queues([], [1]), [1])

if __name__ == '__main__':
    unittest.main()