class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;

        while (r > l) {
            if (numbers[r] + numbers[l] > target) {
                r--;
            }
            else if (numbers[r] + numbers[l] < target) {
                l++;
            }
            else {
                vector<int> output = {l + 1, r + 1};
                return output;
            }
        }
        
    }
};
