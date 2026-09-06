class Solution:

    def encode(self, strs: List[str]) -> str:
        string_codificada = ""
        for i in range(0, len(strs)):
            quantidade_letras = len(strs[i])
            string_codificada += chr(quantidade_letras)
            string_codificada += strs[i]
        print(string_codificada)
        return string_codificada

    def decode(self, s: str) -> List[str]:
        output = []
        string_decodificada = ""
        lista_s = list(s)

        while lista_s != []:
            número_letras = ord(lista_s[0])
            for j in range(1, 1 + número_letras):
                string_decodificada += lista_s[j]
            output.append(string_decodificada)
            string_decodificada = ""
            for j in range(0, 1 + número_letras):
                lista_s.pop(0)
             
        return output


