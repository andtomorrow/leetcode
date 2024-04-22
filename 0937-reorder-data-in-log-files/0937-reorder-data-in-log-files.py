class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        1. letter-logs 다음에 digit-logs
        2. letter-logs는 내용 사전순으로 정렬함. 내용이 같다면 identifier로 정렬
        3. digit-log의 순서는 변경하지 않음
        
        내용이 숫자인지 여부로 digit-log인지 판단.
        split한 뒤, identifier 이후 내용이 숫자면 digit-log임
        """
        digit_logs = []
        letter_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs
                