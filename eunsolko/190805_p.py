scores = [80, 100, 70, 90, 40]

def total(list):
    t_score = 0
    for i in list:
        t_score += i
    return t_score

print(total(scores))

def average(list):
    return total(list) / len(list)

print(average(scores))