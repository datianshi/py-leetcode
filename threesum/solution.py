class Solution:
    #Word Case O(n2)
    def three_sum(self, nums):
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range (0, n-2):
            a = nums[i]
            start = i+1
            end = n-1
            while start < end:
                b = nums[start]
                c = nums[end]
                if a + b + c == 0:
                    if [a,b,c] not in res:
                        res.append([a,b,c])
                    end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start += 1
        return res


    #Average O(n2)
    # def three_sum(self, nums):
    #     nums = sorted(nums)
    #     lookup = dict((v,i) for i,v in enumerate(nums))
    #     n = len(nums)
    #     passed = []
    #     res=[]
    #     for i in range (0, n-2):
    #         for j in range(i+1, n-1):
    #             if (nums[i], nums[j]) in passed:
    #                 continue
    #             else:
    #                 passed.append((nums[i], nums[j]))
    #                 value = -(nums[i] + nums[j])
    #                 index = lookup.get(value,0)
    #                 if index > j:
    #                     res.append([nums[i], nums[j], nums[index]])
    #     return res