class Solution:
    def romanToInt(self, s: str) -> int:
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
        value_int = 0
        for k, v in rom_num_subs.items():
            if k in s:
                s = s.replace(k, '')
                value_int += v
        for char in s:
            value_int += rom_num_info[char]

        return value_int