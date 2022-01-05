class Solution:
    lst1 = []

    def combsum(self, lst, sum, lst2):

        if (sum < 0):
            return
        if (sum == 0):
            if (sorted(lst2) not in self.lst1):
                self.lst1.append(sorted(lst2))
            return
        else:
            for i in lst:
                self.combsum(lst, sum - i, lst2 + [i])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.lst1 = []
        self.combsum(candidates, target, [])
        return self.lst1
