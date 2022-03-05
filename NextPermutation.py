# Solution looks quite complicated so do revise thoroughly
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 0 or len(nums) == 1):
            return
        p = len(nums) - 2
        while (p >= 0 and nums[p] >= nums[p + 1]):
            p -= 1
        if (p >= 0):
            j = len(nums) - 1
            while (nums[p] >= nums[j]):
                j -= 1
            t = nums[p]
            nums[p] = nums[j]
            nums[j] = t
        f = p + 1
        l = len(nums) - 1
        while (f <= l):
            t = nums[f]
            nums[f] = nums[l]
            nums[l] = t
            f += 1
            l -= 1
