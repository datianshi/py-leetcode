import unittest
from twosum.solution import Solution

class TestTwoSum(unittest.TestCase):
    def test_two_sum_1(self):
        nums = [2]
        sl = Solution()
        target = 10
        expected = None
        result = sl.two_sum(nums, target)
        self.assertIsNone(result, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))

    def test_two_sum_2(self):
        nums = [2, 7, 11, 15, 6, 9]
        sl = Solution()
        target = 9
        expected = [0,1]
        result = sl.two_sum(nums, target)
        self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))

    def test_two_sum_3(self):
        nums = [2, 7, 11, 15, 6, 9]
        sl = Solution()
        target = 26
        expected = [2,3]
        result = sl.two_sum(nums, target)
        self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))

    def test_two_sum_4(self):
        nums = [2,7]
        sl = Solution()
        target = 9
        expected = [0,1]
        result = sl.two_sum(nums, target)
        self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))

    def test_two_sum_4(self):
        nums = [2,5,7]
        sl = Solution()
        target = 9
        expected = [0,2]
        result = sl.two_sum(nums, target)
        self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))


unittest.main