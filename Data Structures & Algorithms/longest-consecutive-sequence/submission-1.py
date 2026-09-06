class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            output = 0
            lista_numeros = []
            nums = list(set(nums))
            while nums != []:
                ultimo_numero = min(nums)
                lista_numeros.append(ultimo_numero)
                nums.remove(ultimo_numero)
                                                                                        
                while nums != [] and min(nums) == ultimo_numero + 1:
                    ultimo_numero = min(nums)
                    lista_numeros.append(ultimo_numero)
                    nums.remove(ultimo_numero)
                                                                                                                                                                
                output = max(output, len(lista_numeros))
                lista_numeros = []

            return output
                                                                                                                                                                                            


        