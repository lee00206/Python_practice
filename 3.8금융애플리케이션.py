name = input("사원이름을 입력하세요: ")
workinghr = eval(input("주당 근무시간을 입력하세요: "))
hourwage = eval(input("시간당 급여를 입력하세요: "))
withholdingrate = eval(input("원천징수세율을 입력하세요 "))
taxrate = eval(input("지방세율을 입력하세요: "))

totalwage = workinghr * hourwage

withholding = totalwage * withholdingrate
tax = totalwage * taxrate
totaltax = withholding + tax

finalwage = totalwage - totaltax

print("사원 이름: ", name, "\n", "주당 근무시간: ", workinghr, "\n", "임금: ", hourwage, "\n", "총 급여: ", totalwage, "\n", "공제:", "\n", "   원천징수세 ", "(", withholdingrate*100, "%): ", withholding, "\n", "   주민세 (", taxrate*100, "%): ", tax, "\n", "   총 공제: ", totaltax, "\n", "공제 후 급여: ", finalwage)

