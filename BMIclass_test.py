from BMIclass import BMI

def main():
    bmi = BMI(145, 70)
    print("BMI 수치는", format(bmi.getBMI(), "2.2f"), "이며,", bmi.BMIvalue(), "입니다.")

main()
