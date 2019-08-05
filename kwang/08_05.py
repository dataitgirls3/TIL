my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

my_total_score = 0
for a in my_scores:
	my_total_score += a

print(my_total_score)

#score가 다음과 같은 형태로 주어졌을 때
#scores = [80, 100, 70, 90, 40]
#1. total 함수 만들기
#2. average 함수 만들기
#3. 제대로 했는지 확인하기
#4. 코드를 GitHub에 올리기

scores = [80, 100, 70, 90, 40]

def total(list):
    result = 0
    for i in list:
        result += i
    return result


print(total(scores))


def average(list):
    return sum(list) / len(list)


print(average(scores))
