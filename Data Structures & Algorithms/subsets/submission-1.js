class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        let res = [];
        let subset = [];
        this.dfs(0, nums, subset, res);
        return res;
    }

    dfs(i, nums, subset, res) {
        if (i == nums.length) {
            res.push([...subset]);
            return;
        }

        subset.push(nums[i]);
        this.dfs(i + 1, nums, subset, res);

        subset.pop();
        this.dfs(i + 1, nums, subset, res);

        }

    
}
