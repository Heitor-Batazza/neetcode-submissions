class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_copy = strs.copy()
        lista = []
        listinha = []
        for i in range(0, len(strs)):
            strs_copy[i] = "".join(sorted(strs_copy[i]))
        for i in range(0,len(strs)):
            if type(strs_copy[i]) == str:
                listinha.append(strs[i])
            for j in range(i + 1,len(strs)):
                if strs_copy[i] == strs_copy[j]:
                    listinha.append(strs[j])
                    strs_copy[j] = j
            if listinha != []:
                lista.append(listinha)
            listinha = []
        return lista