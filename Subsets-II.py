# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# lst1=[]
class Solution:
    lst1 = []

    def subsetsWithDup(self, nums):
        self.lst1 = []
        self.subsets(sorted(nums), 0, [])
        print(self.lst1)
        return self.lst1

    def subsets(self, nums, c, s):
        if (c > len(nums) - 1):
            if (s not in self.lst1):
                self.lst1.append(s)
            return
        else:
            self.subsets(nums, c + 1, s)
            self.subsets(nums, c + 1, s + [nums[c]])
