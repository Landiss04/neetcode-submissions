class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ar1 = [0] * 26
        ar2 = [0] * 26

        # build initial frequency
        for i in range(len(s1)):
            ar1[ord(s1[i]) - ord('a')] += 1
            ar2[ord(s2[i]) - ord('a')] += 1

        # slide window
        for i in range(len(s1), len(s2)):
            if ar1 == ar2:
                return True

            # add new char
            ar2[ord(s2[i]) - ord('a')] += 1
            # remove old char
            ar2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        # check last window
        return ar1 == ar2