year = 0

tuition = eval(input("등록금을 입력하세요: "))
increaserate = eval(input("증가율을 입력하세요: "))

tuitiontwice = tuition * 2
increaserate = increaserate / 100

while tuition < tuitiontwice:
    tuition = tuition * (1+increaserate)
    year = year + 1

print("등록금은", year, "년 후에 두 배가 됩니다.")
print(year, "년 후의 등록금은", format(tuition, ".2f"), "원 입니다.")
