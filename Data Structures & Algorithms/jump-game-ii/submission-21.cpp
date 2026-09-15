#include <algorithm>

class Solution {
public:
    int jump(vector<int>& nums) {

        int l = 0;
        int r = 0;
        int output = 0;
        int farthest;

        while (r < nums.size() - 1) {
            farthest = 0;
            for (int i = l; i < r + 1; i++) {
                farthest = max(farthest, i + nums[i]);
            }

            l = r + 1;
            r = farthest;
            output++;
        }
        return output;
        
    }
};
