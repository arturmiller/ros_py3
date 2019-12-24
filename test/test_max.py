#!/usr/bin/env python
import unittest

from ros_py3.run import np_max


class TestMax(unittest.TestCase):

    def test_max(self):
        self.assertEqual(5, np_max([1, 5, 4]))



if __name__ == '__main__':
    import rostest
    rostest.rosrun('ros_py3', 'test_max', TestMax)
