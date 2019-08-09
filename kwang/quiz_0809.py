# score가 다음과 같은 형태로 주어졌을 때

scores = [80, 100, 70, 90, 40]


# total, average 를 만드려고 합니다.


# 1. 테스트 코드 작성하기
# 2. TDD(Test Driven Development)로 함수 만들기
# 3. 코드를 GitHub 에 올리기
# 4. 코드 리뷰

def test_total():
    assert total([80]) == 80
    assert total([80, 20]) == 100
    assert total([80, 100, 70, 90, 40]) == 80 + 100 + 70 + 90 + 40


def test_average():
    assert average(scores) == 76.0


def total(numbers):
    accumulator = 0
    for i in range(len(numbers)):
        accumulator += numbers[i]
    return accumulator
    # return sum(numbers)


print(total(scores))


def average(numbers):
    return sum(numbers) / len(numbers)


print(average(scores))
