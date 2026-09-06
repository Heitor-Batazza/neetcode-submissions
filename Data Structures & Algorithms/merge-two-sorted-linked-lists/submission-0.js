/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let lista1 = [];
        let lista2 = []

        while (list1 !== null) {
            lista1.push(list1.val);
            list1 = list1.next;
        }
        while (list2 !== null) {
            lista2.push(list2.val);
            list2 = list2.next;
        }

        console.log(lista1)
        console.log(lista2)

        for (let i = 0; i < lista2.length; i++) {
            lista1.push(lista2[i])
        }

        let lista1_ordenada = lista1.sort((a, b) => a - b)

        let output = null;
        for (let i = lista1_ordenada.length - 1; i >= 0; i--) {
            output = new ListNode(lista1_ordenada[i], output);
        }
        return output;

        }
}