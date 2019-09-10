scores = [80,100,70,90,40]

def total(n):
    sum=0
    for i in n:
        sum+=i
    return sum

def average(n):
    return total(n)/len(n)

print(total(scores), average(scores))