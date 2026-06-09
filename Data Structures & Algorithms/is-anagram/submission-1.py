class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = {}
        f2 = {}

        if len(s) != len(t):
            return False
        
        for c in s:
            f1[c] = f1.get(c, 0) + 1

        for c in t:
            f2[c] = f2.get(c, 0) + 1

        for key, value in f1.items():
            if key not in f2:
                return False
            elif key in f2 and f2[key] != value:
                return False

        return True