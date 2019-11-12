# Comprehension
## problem 0-1
## 정수 리스트가 주어졌을 때, 각 원소에 1씩 더한 새로운 리스트를 반환하는 함수를 작성하십시오.

x = [1, 2, 3]
def add_1(x):
    return [i+1 for i in x]

## Problem 0-2
## 리스트가 주어졌을 때, 리스트 원소들의 제곱을 구하는 함수를 작성하십시오.

def square(x):
    return [i**2 for i in x]

## Problem 0-3
## 리스트가 주어졌을 때, 리스트 원소들의 제곱의 평균을 구하는 함수를 작성하십시오.

def squared_mean(x):
    return sum(square(x))/len(x)