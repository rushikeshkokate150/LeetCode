class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        dict1 = {}
        for i in strs:
            s = "".join(sorted(i))
            if s not in dict1:
                ans.append([i])
                dict1[s] = len(ans)-1
            else:
                ans[dict1[s]].append(i)
        return ans 