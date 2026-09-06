class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0;

        int l = 0;
        int r = 1;

        while (r < prices.size()) {
            if (prices[r] > prices[l]) {
                int newP = prices[r] - prices[l];
                maxP = max(maxP, newP); 
            } else {
                l = r;
            }
            r++;
        }
        return maxP;
    }
};
