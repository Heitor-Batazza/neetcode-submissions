class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let output = [];
        for (let i = 0; i < nums.length; i++) {
            let valor_i = nums[i];
            nums[i] = 1;
            let output_i = nums.reduce((acumulador, valorAtual) => acumulador * valorAtual, 1);
            output.push(output_i);
            nums[i] = valor_i;
        }
        return output
    }
}
