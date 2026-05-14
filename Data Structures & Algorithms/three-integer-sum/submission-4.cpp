class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> ans = {};

        for (int i = 0; i < nums.size();i++)
        {
            //if (nums.at(i) > 0) break;
            if (i > 0 && nums.at(i) == nums.at(i-1)) continue;

            int lo = i+1, hi = nums.size() -1;
            while (lo < hi)
            {
                int sum = nums.at(i) + nums.at(lo) + nums.at(hi);
                if (sum == 0) 
                {
                    ans.push_back({nums.at(i), nums.at(lo), nums.at(hi)});
                    lo++;
                    hi--;
                    while (lo < hi && nums.at(lo) == nums.at(lo-1)) lo++;
                    while (lo < hi && nums.at(hi) == nums.at(hi+1)) hi--;
                }
                else if (sum > 0) hi--;
                else lo++;
                

            }
        }

        return ans;
    }
};