class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f1 = {}
        f2 = {}
        for num1,num2 in zip(s,t):
            f1[num1] = f1.get(num1, 0) + 1
            f2[num2] = f2.get(num2, 0) + 1
        
        for k,v in f1.items():
            if not f2.get(k):
                return False
            else:
                if v != f2.get(k):
                    return False
        return True
