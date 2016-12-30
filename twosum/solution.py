class Solution:
    def two_sum(self, nums, target):
        lookup = dict((v, i) for i, v in enumerate(nums))
        return next(([i, lookup.get(target - v)]
                     for i, v in enumerate(nums)
                     if lookup.get(target - v, i) != i), None)