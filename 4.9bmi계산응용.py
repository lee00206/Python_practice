weightPound = eval(input("몸무게를 파운드로 입력하세요: "))
heightInch = eval(input("키를 인치로 입력하세요: "))

weightKg = weightPound*0.45359237
heightM = heightInch*0.0254

bmi = weightKg/(heightM**2)

print("BMI는 ", bmi, "입니다.")

if bmi >= 30.0:
    print("비만")
elif bmi >= 25.0:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    bmi < 18.5
    print("저체중")
