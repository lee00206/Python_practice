price = {'배':2000, '사과':1500, '딸기':1800, '참외':2300}
num = {'배':3, '사과':5, '딸기':2, '참외':5}

pear = 0
apple = 0
strawberry = 0
melon = 0

totalNum = pear + apple + strawberry + melon

print('과일 개수를 입력하세요 (최대 5개).')

while totalNum != 5:
    
    pear = int(input('배를 사고 싶은 개수를 입력하세요: '))
    while pear > num['배']:
        print('배를 살 수 있는 개수를 초과하였습니다.')
        pear = int(input('배를 사고 싶은 개수를 다시 입력하세요: '))

    apple = int(input('사과를 사고 싶은 개수를 입력하세요: '))
    while apple > num['사과']:
        print('사과를 살 수 있는 개수를 초과하였습니다.')
        apple = int(input('사과를 사고 싶은 개수를 다시 입력하세요: '))

    strawberry = int(input('딸기를 사고 싶은 개수를 입력하세요: '))
    while strawberry > num['딸기']:
        print('딸기를 살 수 있는 개수를 초과하였습니다.')
        strawberry = int(input('딸기를 사고 싶은 개수를 다시 입력하세요: '))

    melon = int(input('참외를 사고 싶은 개수를 입력하세요: '))
    while melon > num['참외']:
        print('참외를 살 수 있는 개수를 초과하였습니다.')
        melon = int(input('참외를 사고 싶은 개수를 다시 입력하세요: '))

    totalNum = pear + apple + strawberry + melon
    print('과일 개수가 5개가 아닙니다. 다시 입력하세요.')

total = (pear * price['배']) + (apple * price['사과']) + (strawberry * price['딸기']) + (melon * price['참외'])

if pear != 0:
    print('배 {0}개를 사기 위해서는 {1}원이 필요합니다.'.format(pear, pear * price['배']))

if apple != 0:
    print('사과 {0}개를 사기 위해서는 {1}원이 필요합니다.'.format(apple, apple * price['사과']))

if strawberry != 0:
    print('딸기 {0}개를 사기 위해서는 {1}원이 필요합니다.'.format(strawberry, strawberry * price['딸기']))

if melon != 0:
    print('참외 {0}개를 사기 위해서는 {1}원이 필요합니다.'.format(melon, melon * price['참외']))

print('따라서 총 {0}원을 지불하셔야합니다.'.format(total))
