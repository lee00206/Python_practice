weightPound = eval(input("몸무게를 파운드로 입력하세요: "))
heightInch = eval(input("키를 인치로 입력하세요: "))

weightKg = weightPound*0.45359237
heightM = heightInch*0.0254

bmi = weightKg/(heightM**2)

print(bmi)

