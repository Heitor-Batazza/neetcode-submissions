class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let array_s = s.split('')
        let array_t = t.split('')
        let index = 0
        let output = true
        if (s.length != t.length) {
            return false
        }
        for (let i = 0; i < (s.length); i++) {
            if (array_t.includes(array_s[i])) {
                index = array_t.indexOf(array_s[i]);
                array_t.splice(index, 1);
            } else {
                return false
            }
        }
        return output
    }
}
