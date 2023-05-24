class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        combinations_dct = collections.defaultdict(list)
        result_lst = []

        for i in range(len(strs)):
            combinations_dct["".join(sorted(strs[i]))].append(strs[i])

        for k in combinations_dct.keys():
            result_lst.append(combinations_dct[k])

        return result_lst