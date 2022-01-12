class Solution:
    lst1 = []

    def combsum(self,lst,ind, sum, lst2):

        if (sum < 0):
            return
        if (sum == 0):
            if(sorted(lst2) not in self.lst1):
                self.lst1.append(sorted(lst2))
            return
        if (ind >= len(lst)):
            print(lst2," ",sum)
            return

        else:
                self.combsum(lst,ind+1, sum,lst2)
                self.combsum(lst,ind+1,sum-lst[ind],lst2+[lst[ind]])

    def combinationSum(self, candidates,target):
        self.lst1 = []
        self.combsum(candidates,0,target, [])
        return self.lst1
s=Solution()
print(s.combinationSum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
,27))
