class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        cnt_most_common = Counter(words).most_common(1)

        return cnt_most_common[0][0]