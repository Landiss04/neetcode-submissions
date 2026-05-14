class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int lo = 0;
        int hi = numbers.size() -1;

        while (lo < hi)
        {
            int temp_sum = numbers[lo] + numbers[hi];
            if (temp_sum == target) return {lo+1, hi+1};
            else if (temp_sum > target) hi--;
            else if (temp_sum < target) lo++;
        }

        return {};
    }
};
