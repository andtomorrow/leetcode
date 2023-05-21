class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            body = log.split(maxsplit=1)[1]
            # id = log.split()[0]
            elm = body.split()
            if "".join(elm).isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split(maxsplit=1)[1], x.split()[0]))
        return letter_logs + digit_logs