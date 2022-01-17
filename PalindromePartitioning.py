class Solution:
    def isPalindrome(self, s):
        first = 0
        last = len(s) - 1
        while (first <= last):
            if (s[first] != s[last]):
                return False
            first += 1
            last -= 1
        return True

    def Breaking(self, s, ind, ans, ds):
        if (ind == len(s)):
            ans.append(ds)
            return
        for i in range(ind, len(s)):
            if (self.isPalindrome(s[ind:i + 1])):
                self.Breaking(s, i + 1, ans, ds + [s[ind:i + 1]])

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.Breaking(s, 0, ans, [])
        return ans
