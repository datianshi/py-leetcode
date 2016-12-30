import unittest
from threesum.solution import Solution

class TestThreeSum(unittest.TestCase):
    def test_three_sum_1(self):
        s = [-1,0,1,2,-1,-4]
        sl = Solution()
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = sl.three_sum(s)
        self.assertListEqual(result, expected, "With nums: {} and the result: {} expects as {}".format(s, result, expected))

    def test_three_sum_2(self):
        s = [0,0,0]
        sl = Solution()
        expected = [[0,0,0]]
        result = sl.three_sum(s)
        self.assertListEqual(result, expected, "With nums: {} and the result: {} expects as {}".format(s, result, expected))

    def test_three_sum_3(self):
        s = [0, 0, 0, 0]
        sl = Solution()
        expected = [[0, 0, 0]]
        result = sl.three_sum(s)
        self.assertListEqual(result, expected,
                             "With nums: {} and the result: {} expects as {}".format(s, result, expected))

            # def test_three_sum_2(self):
    #     nums = [2, 7, 11, 15, 6, 9]
    #     sl = Solution()
    #     target = 9
    #     expected = [0,1]
    #     result = sl.three_sum(nums, target)
    #     self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))
    #
    # def test_three_sum_3(self):
    #     nums = [2, 7, 11, 15, 6, 9]
    #     sl = Solution()
    #     target = 26
    #     expected = [2,3]
    #     result = sl.three_sum(nums, target)
    #     self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))
    #
    # def test_three_sum_4(self):
    #     nums = [2,7]
    #     sl = Solution()
    #     target = 9
    #     expected = [0,1]
    #     result = sl.three_sum(nums, target)
    #     self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))
    #
    # def test_three_sum_4(self):
    #     nums = [2,5,7]
    #     sl = Solution()
    #     target = 9
    #     expected = [0,2]
    #     result = sl.three_sum(nums, target)
    #     self.assertListEqual(result, expected, "With nums: {} and target {} it should return index as {}".format(nums, target, expected))


unittest.main