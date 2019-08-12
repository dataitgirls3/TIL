class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]

# 1. class_total(class_socres, '국어') == 170
# 2. class_total_all(classs_scores) == 430


def class_total(scores, subject):
    total = 0
    for dic in scores:
        total += dic[subject]
    return total


def class_total_all(scores):
    total = 0
    for dic in scores:
        for num in dic.values():
            total += num
    return total


def test_class_total():

    assert class_total(class_scores, '국어') == 80 + 90
    assert class_total_all(class_scores) == 430

