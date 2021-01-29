x1, y1 = eval(input("첫 번째 점에 대한 x1과 y1을 입력하세요: "))

x2, y2=eval(input("두 번째 점에 대한 x2와 y2를 입력하세요: "))

distance = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5

print("두 점 사이의 거리는", distance, "입니다.")
