class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        rm_dupl = list(dict.fromkeys(letters))
        for i in range(len(rm_dupl)):
            if rm_dupl[i] > target:
                if rm_dupl[i]:
                    return rm_dupl[i]
        
        return rm_dupl[0]