class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::unordered_map<int,int> n;
        for (int i : nums) n[i]++;
        
        for (auto pair : n)
        {
            if (pair.second == 1) return pair.first;  
        }
        return 0;
    }
};
