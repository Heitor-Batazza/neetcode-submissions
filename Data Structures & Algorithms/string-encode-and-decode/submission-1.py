class Solution:

    def encode(self, strs: List[str]) -> str:
        string_codificada = ""
        for i in range(0, len(strs)):
            string_codificada += strs[i]
            string_codificada += "§"
        print(string_codificada)
        return string_codificada

    def decode(self, s: str) -> List[str]:
        output = []
        string_decodificada = ""
        lista_s = list(s)
        for caractere in lista_s:
            if caractere != "§":
                string_decodificada += caractere
            else:
                output.append(string_decodificada)
                string_decodificada = ""
        return output


