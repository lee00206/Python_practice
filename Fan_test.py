from Fan import Fan

def main():
    fan1 = Fan()
    fan1.fanspeed(3)
    fan1.fanradius(10)
    fan1.fancolor
    fan1.turnOn()

    fan2 = Fan()
    fan2.fanspeed(2)
    fan2.radius
    fan2.color
    fan2.turnOff()

    print("fan1:\n \t속도: ", fan1.fanspeed(3),"\n\t크기: ", fan1.fanradius(10), "\n\t색상: ", fan1.fancolor("yellow"), "\n\t전원: ", fan1.turnOn())
    print("fan2:\n \t속도: ", fan2.fanspeed(2),"\n\t크기: ", fan2.fanradius(5), "\n\t색상: ", fan2.fancolor("blue"), "\n\t전원: ", fan2.turnOff())

main()
