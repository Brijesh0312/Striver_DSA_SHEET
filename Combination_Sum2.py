class Solution:
    def combsumII(self, lst, ind, target, ds, ans):
        if (target == 0):
            ans.append(ds)
            return
        else:
            for i in range(ind, len(lst)):
                if (i > ind and lst[i] == lst[i - 1]):
                    continue
                elif (lst[i] > target):
                    break

                self.combsumII(lst, i + 1, target - lst[i], ds + [lst[i]], ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.combsumII(sorted(candidates), 0, target, [], ans)
        return ans
