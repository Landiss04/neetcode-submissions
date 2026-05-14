class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> sums;

        for (int i = 0;i < nums.size();i++) {
            int needed = target - nums[i];
            auto it = sums.find(needed);
            if (it != sums.end()) {
                return {it->second, i};
            }
            sums[nums[i]] = i;
        }
        return {};
    }
};
