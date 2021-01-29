import random

answer = []
student1 = []
student2 = []
student3 = []
student4 = []
student5 = []


def Rand(start, end, num):
    for i in range(0, 10):
        answer.append(random.randint(start, end))
        student1.sppend(random.randint(start, end))
        student2.sppend(random.randint(start, end))
        student3.sppend(random.randint(start, end))
        student4.sppend(random.randint(start, end))
        student5.sppend(random.randint(start, end))

    return answer, student1, student2, student3, student4, student5
