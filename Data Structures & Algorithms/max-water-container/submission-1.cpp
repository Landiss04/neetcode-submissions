class Solution {
public:
    int maxArea(vector<int>& heights) {
        int lo = 0;
        int hi = heights.size() - 1;

        int max_area = 0;

        while (lo < hi) {

            int area = (hi - lo) * min(heights[lo], heights[hi]);

            max_area = max(max_area, area);

            if (heights[lo] < heights[hi]) {
                lo++;
            }
            else {
                hi--;
            }
        }

        return max_area;
    }
};