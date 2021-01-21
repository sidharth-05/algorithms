class Solution:
    from collections import Counter
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for k in zip(*strs):
            if len(Counter(k).values()) == 1:
                res += k[0]
            else:
                break
        return res  