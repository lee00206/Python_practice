import random

you = eval(input("가위(0), 바위(1), 보(2): "))
computer = random.randint(0,2)

if you == computer:
    print("비겼습니다.")
elif you == 0:
    if computer == 1:
        print("컴퓨터는 바위 입니다. 당신은 가위 입니다. 당신이 졌습니다.")
    else:
        print("컴퓨터는 보 입니다. 당신은 가위 입니다. 당신이 이겼습니다.")
elif you == 1:
    if computer == 0:
        print("컴퓨터는 가위 입니다. 당신은 바위 입니다. 당신이 이겼습니다.")
    else:
        print("컴퓨터는 보 입니다. 당신은 바위 입니다. 당신이 졌습니다.")
else:
    you == 2
    if computer == 0:
        print("컴퓨터는 가위 입니다. 당신은 보 입니다. 당신이 졌습니다.")
    else:
        print("컴퓨터는 바위 입니다. 당신은 보 입니다. 당신이 이겼습니다.")

