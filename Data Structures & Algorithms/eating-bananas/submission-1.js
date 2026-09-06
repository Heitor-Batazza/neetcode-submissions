class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let k = 0;
        let href = h + 1;
        while (href > h) {
            k += 1;
            href = 0;
            for (let i = 0; i < piles.length; i++) {
                href += Math.ceil(piles[i] / k);
                if (href > h) {
                    break
                }
            }
        }
        return k
    }
}
