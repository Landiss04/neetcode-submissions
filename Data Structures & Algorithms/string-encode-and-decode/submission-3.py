class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(num + "`" for num in strs)

    def decode(self, s: str) -> List[str]:
        temp = ""
        ans = []
        for i in range(len(s)):
            if s[i] == "`":
                ans.append(temp)
                temp = ""
            else:
                temp += s[i]
        return ans
            