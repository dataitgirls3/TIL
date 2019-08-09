my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

my_total_score = 0

for score in my_scores:
	my_total_score += score

print("내총점: ", my_total_score)

# score가 다음과 같은 형태로 주어졌을 때
scores = [80, 100, 70, 90, 40]


#1. total 함수 만들기
def total(numbers):
    result = 0
    for i in numbers:
        result += i
        return result
    
    
    
# 2. average 함수 만들기
def average(numbers):
    return total(numbers) / len(numbers)
    
    
# 3. 제대로 했는지 확인하기
print("총점 : ", total(scores))
print("평점: ", average(scores))
    
# 4. 코드를 GitHub에 올리기