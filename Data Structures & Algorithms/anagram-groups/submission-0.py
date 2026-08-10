class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = defaultdict(list)
        for val in strs:
            temp = [0] * 26
            for c in val:
                temp[ord(c) - ord('a')] += 1
            res[tuple(temp)].append(val)
        return list(res.values())

