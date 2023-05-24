class Solution:
    def intToRoman(self, num: int) -> str:
        rom_num_info = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        rom_num_subs = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        rom_nums_lst = [*rom_num_info.items(), *rom_num_subs.items()]
        rom_nums_lst = sorted(rom_nums_lst, key=lambda x: x[1], reverse=True)
        rom_nums_dct = {x[0]:x[1] for x in rom_nums_lst}
        
        num_roman = ''

        for k, v in rom_nums_dct.items():
            quotient, remainder = divmod(num, v)
            if quotient:
                num_roman += k*quotient
            num = remainder
        
        return num_roman
        
        
        
        
        
        