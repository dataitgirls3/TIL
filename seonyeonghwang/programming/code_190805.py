scores = [80, 100, 70, 90, 40]

# total 함수 만들기

def total(scores):
    total_scores = 0
    for score in scores:
        total_scores += score
    return total_scores
print(total(scores))

# average 함수 만들기

def average(scores):
    average_scores = 0
    for score in scores:
        average_scores = total(scores)/len(scores)
    return average_scores
print(average(scores))