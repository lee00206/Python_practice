seconds = eval(input("초 값을 정수로 입력하세요: "))

minutes = seconds // 60
remainingSeconds = seconds % 60
print(seconds, "초는", minutes, "분과", remainingSeconds, "초입니다.")
