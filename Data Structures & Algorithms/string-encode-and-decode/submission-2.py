class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for i in strs:
            sol += i
            sol += "."
        return sol
    def decode(self, s: str) -> List[str]:
        sol = []
        temp = ""
        for i in range(0, len(s)):
            if s[i] == ".":
                sol.append(temp)
                temp = ""
            else:
                temp += s[i]

        return sol
        