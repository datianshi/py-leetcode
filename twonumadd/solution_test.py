import unittest
from twonumadd.solution import Solution, IterListNodes

class TestAddTwoNums(unittest.TestCase):
    def test_iterate_list_node(self):
        list=[4,6,7]
        node = Solution.new_list_nodes(list)
        for i,x in enumerate(IterListNodes(node)):
            self.assertEqual(x,list[i])

    def test_equal_two_list_node(self):
        node1 = Solution.new_list_nodes([4, 6, 7])
        node2 = Solution.new_list_nodes([4, 8, 7])
        node3 = Solution.new_list_nodes([4, 6, 7])
        self.assertEqual(node1, node3)
        self.assertNotEqual(node1, node2)

    def test_add_two_nums_1(self):
        node1 = Solution.new_list_nodes([4, 5, 6])
        node2 = Solution.new_list_nodes([7, 8, 9])
        expect = Solution.new_list_nodes([1,4,6,1])
        result = Solution.two_sum_nums(node1, node2)
        self.assertIsNotNone(result, "{}".format(result))
        self.assertEqual(result, expect, "{} + {} != {}".format(node1, node2, result))

    def test_add_two_nums_2(self):
        node1 = Solution.new_list_nodes([9, 9, 9])
        node2 = Solution.new_list_nodes([1])
        expect = Solution.new_list_nodes([0,0,0,1])
        result = Solution.two_sum_nums(node1, node2)
        self.assertIsNotNone(result, "{}".format(result))
        self.assertEqual(result, expect, "{} + {} != {}".format(node1, node2, result))

    def test_add_two_nums_3(self):
        node1 = Solution.new_list_nodes([9])
        node2 = Solution.new_list_nodes([1])
        expect = Solution.new_list_nodes([0,1])
        result = Solution.two_sum_nums(node1, node2)
        self.assertIsNotNone(result, "{}".format(result))
        self.assertEqual(result, expect, "{} + {} != {}".format(node1, node2, result))

    def test_add_two_nums_4(self):
        node1 = Solution.new_list_nodes([2,4,3])
        node2 = Solution.new_list_nodes([5,6,4])
        expect = Solution.new_list_nodes([7,0,8])
        result = Solution.two_sum_nums(node1, node2)
        self.assertIsNotNone(result, "{}".format(result))
        self.assertEqual(result, expect, "{} + {} != {}".format(node1, node2, result))

unittest.main