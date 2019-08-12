# 1. total 함수
# 2. average 함수
scores = [100, 40, 50, 14, 40, 90, 49]

def total(numbers):
    total_num = 0
    for num in numbers:
        total_num += num
    return total_num

def average(numbers):
    return total(numbers) / len(numbers)


def test_total_only_one():
    assert total([80]) == 80
    assert total([20]) == 20


def test_average():
    assert average([20]) == 20


print(total(scores))
print(average(scores))


def multiply(x, y):
    return f'{x} * {y} = {x * y}'


def test_multiply():
    assert multiply(2, 1) == '2 * 1 = 2'
    assert multiply(2, 2) == '2 * 2 = 4'


print(multiply(1, 2))

# 딕셔너리
def test_dictionary():
    sco = {
        '국어' : 10,
        '영어' : 20,
        '수학' : 30
    }
    assert sco['국어'] == 10
    assert sco['영어'] == 20
    assert sco['수학'] == 30
