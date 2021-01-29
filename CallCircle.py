from Circle import Circle

def main():
    circle1 = Circle()
    print("반지름이 ", circle1.radius, "인 원의 넓이는 ", format(circle1.getArea(), "4.2f"), "입니다.")

    circle2 = Circle(25)
    print("반지름이 ", circle2.radius, "인 원의 넓이는 ", format(circle2.getArea(), "4.2f"), "입니다.")

    circle3 = Circle(125)
    print("반지름이 ", circle3.radius, "인 원의 넓이는 ", format(circle3.getArea(), "4.2f"), "입니다.")

    circle2.radius = 100
    print("반지름이 ", circle2.radius, "인 원의 넓이는 ", format(circle2.getArea(), "4.2f"), "입니다.")


main()
