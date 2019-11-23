scores = [80, 100, 70, 90, 40]

def total(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    return total

def test_total():
    assert total([80]) == 80
    assert total([80, 20]) == 100
    assert total([80, 10, 30]) == 120

def average(scores):
    return total(scores)/len(scores)

def test_average():
    assert average([80]) == 80
    assert average([80, 100]) == 90
    assert average([20, 20, 50]) == 30







