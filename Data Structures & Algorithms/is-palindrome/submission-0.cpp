class Solution {
public:
    bool isPalindrome(string s) {
        int lo = 0;
        int hi = s.length() - 1;

        while (lo < hi) {

            if (!isalnum(s[lo])) {
                lo++;
            }
            else if (!isalnum(s[hi])) {
                hi--;
            }
            else if (tolower(s[lo]) == tolower(s[hi])) {
                lo++;
                hi--;
            }
            else {
                return false;
            }
        }

        return true;
    }
};